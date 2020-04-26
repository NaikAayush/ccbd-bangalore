#!/usr/bin/python3
# pylint: disable=missing-function-docstring,global-statement,redefined-outer-name

import sys
import subprocess
import multiprocessing as multiprocessing

try:
    green_threshold = sys.argv[1]
except IndexError:
    green_threshold = 50.0

def run_reduce_task(green_threshold, inp_file, out_file, separator="| "):
    file_opened_here = False
    if isinstance(out_file, str):
        out_file = open(out_file, "w", encoding="utf8")
        file_opened_here = True
    current_location = None
    current_green = 0
    current_count = 0
    def reduce_task(inp, outfile):
        nonlocal current_location, current_green, current_count
        pincode_locality, green = inp.split(separator)
        green = float(green)
        if current_location == pincode_locality:
            # print("Rolling average for {}: ({} + {})/2".format(pincode_locality, current_green, green), file=sys.stderr)
            current_green += green
            current_count += 1
            # print("increasing count:", current_count, file=sys.stderr)
        else:
            # print("Inside else:", current_location, current_green, green_threshold)
            if current_location:
                green_percentage = current_green/current_count
                if green_percentage > green_threshold:
                    print("{} {}".format(current_location, green_percentage), file=outfile)
                    # print("Writing to file:", outfile, file=sys.stderr)
                    outfile.flush()
            current_location = pincode_locality
            current_green = green
            current_count = 1
        return current_location, current_green, current_count
    last_location = None
    last_green = 0
    last_count = 0
    total_count = 0
    for line in inp_file:
        line = line.strip()
        last_location, last_green, last_count = reduce_task(line, out_file)
        total_count += 1
    if current_location == last_location:
        green_percentage = current_green/current_count
        if green_percentage > green_threshold:
            print("{} {}".format(current_location, green_percentage), file=out_file)
            out_file.flush()
    # print("Processed {} rows in process {}".format(total_count,
                                                   # multiprocessing.current_process().name),
          # file=sys.stderr)
    out_file.flush()
    # print("Flushed to file:", out_file, file=sys.stderr)
    if file_opened_here:
        out_file.close()

def sort_file(filename):
    subprocess.call(["sort", "-k1,1", filename, "-o", filename])

def run_reduce_task_multi(green_threshold, inp_filenames, num_files, out_filename):
    sort_jobs = []
    for in_filename in inp_filenames:
        p = subprocess.Popen(["sort", "-k1,1", in_filename, "-o", in_filename])
        sort_jobs.append(p)
    for sort_job in sort_jobs:
        sort_job.communicate()
        sort_job.wait()
    print([job.poll() for job in sort_jobs])
    inp_files = [open(filename, "r", encoding="utf8") for filename in inp_filenames]
    print("Reducer input files:", inp_filenames)
    out_filenames = ["{0}{1:02d}".format(out_filename, i) for i in range(num_files)]
    print("Reducer temp output files:", out_filenames)
    jobs = []
    for inp_file, out_file in zip(inp_files, out_filenames):
        print("Starting process for input {}, output {}".format(inp_file, out_file))
        p = multiprocessing.Process(target=run_reduce_task,
                                    args=(0.0, inp_file, out_file))
        p.start()
        jobs.append(p)
    for job in jobs:
        job.join()
    for in_file in inp_files:
        in_file.close()
    temp_filename = "reduce_out_temp"
    out_files = [open(filename, "r", encoding="utf8") for filename in out_filenames]
    with open(temp_filename, "w", encoding="utf8") as temp_file:
        for out_file in out_files:
            out_file.seek(0)
            temp_file.write(out_file.read())
            # temp_file.write("\n")
            temp_file.flush()
    for out_file in out_files:
        out_file.close()
    sort_file(temp_filename)
    with open(out_filename, "w", encoding="utf8") as out_file:
        with open(temp_filename, "r", encoding="utf8") as in_file:
            run_reduce_task(green_threshold, in_file, out_file, separator=" ")

if __name__ == "__main__":
    inp_file = sys.stdin
    out_file = sys.stdout
    run_reduce_task(green_threshold, inp_file, out_file)
