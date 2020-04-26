import time
import subprocess
import csv
from flask import Flask, render_template, request
import mapper
import reducer_rollingavg as reducer

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        start_time = time.time()
        green_percentage = request.form["green_percentage"]
        green_percentage = float(green_percentage)
        print("Using green_percentage:", green_percentage)
        if "multithreaded" in request.form:
            multithreaded = True
        else:
            multithreaded = False
        if not multithreaded:
            with open("bigfile.csv", "rt") as input_file:
                with open("output.csv", "wt") as output_file:
                    print("Running mapper")
                    with open("mapper_out", "wt") as mapper_out:
                        mapper.run_map_task(input_file, mapper_out)
                    subprocess.call(["sort", "-k1,1", "mapper_out", "-o", "mapper_out"])
                    print("Runnnng reducer")
                    with open("mapper_out", "rt") as mapper_out:
                        reducer.run_reduce_task(green_percentage, mapper_out, output_file)
        else:
            cores = 8
            mapper_outfiles = mapper.run_map_task_multi("bigfile.csv", cores, "temp_mapper_out")
            reducer.run_reduce_task_multi(green_percentage, mapper_outfiles, cores, "output.csv")
        outputs = []
        with open("output.csv", "rt") as output_file:
            reader = csv.reader(output_file, delimiter=" ")
            for row in reader:
                outputs.append(row)
        time_taken = round(time.time() - start_time, 5)
        return render_template("index.html",
                               outputs=outputs,
                               green_percentage=str(green_percentage),
                               time_taken=time_taken,
                               multithreaded=multithreaded)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
