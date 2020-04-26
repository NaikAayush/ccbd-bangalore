import time
import subprocess
import csv
from flask import Flask, render_template, request, session
import mapper
import reducer_rollingavg as reducer

app = Flask(__name__)
app.secret_key = "hmm secret key"

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
        if not multithreaded:
            with open("main.csv", "rt",encoding="utf8") as input_file:
                with open("output.csv", "wt",encoding="utf8") as output_file:
                    print("Running mapper")
                    with open("mapper_out", "wt",encoding="utf8") as mapper_out:
                        mapper.run_map_task(input_file, mapper_out)
                    subprocess.call(["sort", "-k1,1", "mapper_out", "-o", "mapper_out"])
                    print("Runnnng reducer")
                    with open("mapper_out", "rt",encoding="utf8") as mapper_out:
                        reducer.run_reduce_task(green_percentage, mapper_out, output_file)
        else:
            cores = 8
            mapper_outfiles = mapper.run_map_task_multi("main.csv", cores, "temp_mapper_out")
            reducer.run_reduce_task_multi(green_percentage, mapper_outfiles, cores, "output.csv")
        outputs = []
        with open("output.csv", "rt",encoding="utf8") as output_file:
            reader = csv.reader(output_file, delimiter=" ")
            for row in reader:
                outputs.append(row)
        time_taken = round(time.time() - start_time, 5)
        return render_template("mapRed.html",
                               outputs=outputs,
                               green_percentage=str(green_percentage),
                               time_taken=time_taken,
                               multithreaded=multithreaded)
    return render_template("mapRed.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
