import os
import time
import subprocess
import csv
from flask import Flask, render_template, request, session
import pandas as pd

import mapper
import reducer

app = Flask(__name__)
app.secret_key = "hmm secret key"

pincode_locality_mapper = pd.read_csv("./pincode_locality_mapping.csv", header=None)
pincode_locality_mapper.set_index(0, inplace=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/mapred", methods=["GET", "POST"])
def mapRed():
    if request.method == "POST":
        start_time = time.time()

        green_percentage = request.form["green_percentage"]
        green_percentage = float(green_percentage)
        print("Using green_percentage:", green_percentage)

        multithreaded = "multithreaded" in request.form
        hadoop = "hadoop" in request.form
        groupby = request.form["groupby"]
        groupby_pincode = groupby == "pincode"

        inp_filename = "FINAL_DATA_FILTERED.csv"
        if not hadoop:
            output_filename = "output.csv"
            if not multithreaded:
                with open(inp_filename, "rt", encoding="utf8") as input_file:
                    with open("output.csv", "wt", encoding="utf8") as output_file:
                        print("Running mapper")
                        with open("mapper_out", "wt", encoding="utf8") as mapper_out:
                            mapper.run_map_task(input_file, mapper_out, groupby_pincode)
                        subprocess.call(["sort", "-k1,1", "mapper_out", "-o", "mapper_out"])
                        print("Runnnng reducer")
                        with open("mapper_out", "rt", encoding="utf8") as mapper_out:
                            reducer.run_reduce_task(green_percentage, mapper_out, output_file)
            else:
                cores = 8
                mapper_outfiles = mapper.run_map_task_multi(inp_filename,
                                                            cores,
                                                            "temp_mapper_out",
                                                            groupby_pincode)
                reducer.run_reduce_task_multi(green_percentage,
                                              mapper_outfiles,
                                              cores,
                                              output_filename)
        else:
            env = os.environ.copy()
            env["GREEN_THRESHOLD"] = str(green_percentage)
            env["GROUPBY_PINCODE"] = "1" if groupby_pincode else "0"
            hadoop_process = subprocess.Popen(["sh", "-c",
                                               "./run_hadoop.sh " + inp_filename],
                                              env=env)
            hadoop_process.communicate()
            if hadoop_process.poll() is not None:
                print("Hadoop is done with poll", hadoop_process.poll())
            output_filename = "output/part-00000"
        outputs = []
        with open(output_filename, "rt", encoding="utf8") as output_file:
            reader = csv.reader(output_file, delimiter="|")
            if groupby_pincode:
                for row in reader:
                    pincode = row[0]
                    locations = []
                    for sub_district, district in zip(pincode_locality_mapper.loc[[pincode]][1],
                                                      pincode_locality_mapper.loc[[pincode]][2]):
                        locations.append((sub_district, district))
                    outputs.append([row[0], locations, row[1].strip()])
            else:
                for row in reader:
                    pincode, sub_district, district = row[0].split(",")
                    green = row[1].strip()
                    outputs.append([pincode, [(sub_district, district)], green])

        time_taken = round(time.time() - start_time, 5)
        return render_template("mapRed.html",
                               outputs=outputs,
                               green_percentage=str(green_percentage),
                               time_taken=time_taken,
                               multithreaded=multithreaded,
                               hadoop=hadoop,
                               groupby=groupby)
    return render_template("mapRed.html", outputs=None)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
