import subprocess
import csv
from flask import Flask, render_template, request
import mapper
import reducer_rollingavg as reducer

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/mapred", methods=["GET", "POST"])
def mapRed():
    if request.method == "POST":
        green_percentage = request.form["green_percentage"]
        green_percentage = float(green_percentage)
        print("Using green_percentage:", green_percentage)
        with open("main.csv", "rt") as input_file:
            with open("output.csv", "wt") as output_file:
                print("Running mapper")
                with open("mapper_out", "wt") as mapper_out:
                    mapper.run_map_task(input_file, mapper_out)
                subprocess.call(["sort", "-k1,1", "mapper_out", "-o", "mapper_out"])
                print("Runnnng reducer")
                with open("mapper_out", "rt") as mapper_out:
                    reducer.run_reduce_task(green_percentage, mapper_out, output_file)
        outputs = []
        with open("output.csv", "rt") as output_file:
            reader = csv.reader(output_file, delimiter=" ")
            for row in reader:
                outputs.append(row)
        return render_template("mapRed.html", outputs=outputs, green_percentage=str(green_percentage))
    return render_template("mapRed.html")

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
