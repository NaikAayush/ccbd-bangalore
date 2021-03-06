#!/usr/bin/python3
# pylint: disable=missing-function-docstring,global-statement,redefined-outer-name

import os
import sys
import csv
import subprocess
import multiprocessing
from reducer import sort_file

def run_map_task(inp_file, out_file, groupby_pincode=True):
    def map_task_pincode(row):
        green = row[3].strip() or "0.0"
        pincode = row[6]
        return "{}| {}".format(pincode, green)
    def map_task_locality(row):
        loc1 = row[4]
        loc2 = row[5]
        green = row[3].strip() or "0.0"
        pincode = row[6]
        return "{},{},{}| {}".format(pincode, loc1, loc2, green)
    reader = csv.reader(inp_file, delimiter=",", quotechar='"')
    if groupby_pincode:
        map_task = map_task_pincode
    else:
        map_task = map_task_locality
    for row in reader:
        map_out = map_task(row)
        print(map_out, file=out_file)
        out_file.flush()

def run_map_task_multi(inp_filename, num_files, out_file_prefix, groupby_pincode=True):
    sort_file(inp_filename)
    subprocess.call(["split", "--number=l/{}".format(num_files), "-d", inp_filename, inp_filename])
    in_filenames = ["{0}{1:02d}".format(inp_filename, i) for i in range(num_files)]
    in_files = [open(filename, "r", encoding="utf8") for filename in in_filenames]
    out_filenames = ["{0}{1:02d}".format(out_file_prefix, i) for i in range(num_files)]
    out_files = [open(filename, "w", encoding="utf8") for filename in out_filenames]
    jobs = []
    for in_file, out_file in zip(in_files, out_files):
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
