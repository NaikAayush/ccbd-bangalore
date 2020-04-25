#!/usr/bin/python3
# pylint: disable=missing-function-docstring,global-statement,redefined-outer-name

import sys
import csv

def map_task(row):
    pincode = row[4]
    locality = row[3]
    green = row[5]
    return "{},{}| {}".format(pincode, locality, green)

if __name__ == "__main__":
    inp_file = sys.stdin
    out_file = sys.stdout
    reader = csv.reader(inp_file, delimiter=",", quotechar='"')
    for row in reader:
        map_out = map_task(row)
        print(map_out, file=out_file)
