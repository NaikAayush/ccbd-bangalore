#!/usr/bin/python3
# pylint: disable=missing-function-docstring,global-statement,redefined-outer-name

import os
import sys
import csv
import subprocess
import multiprocessing as multiprocessing
from reducer_rollingavg import sort_file

def run_map_task(inp_file, out_file, groupby_pincode=True):
    def map_task_pincode(row):
        green = row[5]
        pincode = row[6]
        return "{}| {}".format(pincode, green)
    def map_task_locality(row):
        loc1 = row[3]
        loc2 = row[4]
        green = row[5]
        pincode = row[6]
        return "{},{},{}| {}".format(pincode, loc1, loc2, green)
    reader = csv.reader(inp_file, delimiter=",", quotechar='"')
    # print("Processing in process:", multiprocessing.current_process().name)
    if groupby_pincode:
        map_task = map_task_pincode
    else:
        map_task = map_task_locality
    for row in reader:
        map_out = map_task(row)
        # print("Processing a row in process:", multiprocessing.current_process().name)
        print(map_out, file=out_file)
        # out_file.write(map_out+"\n")
        out_file.flush()

def run_map_task_multi(inp_filename, num_files, out_file_prefix, groupby_pincode=True):
    sort_file(inp_filename)
    subprocess.call(["split", "--number=l/{}".format(num_files), "-d", inp_filename, inp_filename])
    in_filenames = ["{0}{1:02d}".format(inp_filename, i) for i in range(num_files)]
    # print("Input files:", in_filenames)
    in_files = [open(filename, "r", encoding="utf8") for filename in in_filenames]
    out_filenames = ["{0}{1:02d}".format(out_file_prefix, i) for i in range(num_files)]
    # print("Output files:", out_filenames)
    out_files = [open(filename, "w", encoding="utf8") for filename in out_filenames]
    jobs = []
    for in_file, out_file in zip(in_files, out_files):
        # print("Starting process for input {}, output {}".format(in_file, out_file))
        p = multiprocessing.Process(target=run_map_task, args=(in_file, out_file, groupby_pincode))
        p.start()
        jobs.append(p)
    for job in jobs:
        job.join()
    print("Closing output files")
    for out_file in out_files:
        out_file.close()
    print("Closing input files")
    for in_file in in_files:
        in_file.close()
    return out_filenames

if __name__ == "__main__":
    groupby_pincode = bool(int(os.getenv("GROUPBY_PINCODE")))
    inp_file = sys.stdin
    out_file = sys.stdout
    run_map_task(inp_file, out_file, groupby_pincode)
