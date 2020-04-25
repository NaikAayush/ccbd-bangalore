#!/usr/bin/python3
# pylint: disable=missing-function-docstring,global-statement,redefined-outer-name

import sys

green_threshold = 65.0

current_location = None
current_green = 0
current_count = 0
def reduce_task(inp, outfile):
    global current_location, current_green, current_count
    pincode_locality, green = inp.split("| ")
    green = float(green)
    if current_location == pincode_locality:
        current_green = (current_green + green) / 2
        current_count += 1
    else:
        if current_location:
            green_percentage = current_green
            if green_percentage > green_threshold:
                print("{} {}".format(current_location, green_percentage), file=outfile)
        current_location = pincode_locality
        current_green = green
        current_count = 1
    return current_location, current_green, current_count

if __name__ == "__main__":
    inp_file = sys.stdin
    out_file = sys.stdout
    last_location = None
    last_green = 0
    last_count = 0
    for line in sys.stdin:
        line = line.strip()
        last_location, last_green, last_count = reduce_task(line, out_file)
    if current_location == last_location:
        green_percentage = current_green
        if green_percentage > green_threshold:
            print("{} {}".format(current_location, green_percentage), file=out_file)
