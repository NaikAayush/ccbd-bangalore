import csv
from flask import Flask, render_template, request
import mapper
import reducer_rollingavg as reducer

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        green_percentage = request.form["green_percentage"]
        green_percentage = float(green_percentage)
        print("Using green_percentage:", green_percentage)
        with open("main.csv", "rt") as input_file:
            with open("mapper_out", "wt+") as mapper_out:
                with open("output.csv", "wt") as output_file:
                    print("Running mapper")
                    mapper.run_map_task(input_file, mapper_out)
                    mapper_out.seek(0)
                    print("Runnnng reducer")
                    reducer.run_reduce_task(green_percentage, mapper_out, output_file)
        outputs = []
        with open("output.csv", "rt") as output_file:
            reader = csv.reader(output_file, delimiter=" ")
            for row in reader:
                outputs.append(row)
        return render_template("index.html", outputs=outputs, green_percentage=green_percentage)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
