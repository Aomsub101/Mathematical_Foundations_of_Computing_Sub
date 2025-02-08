from flask import Flask, render_template, request
from algorithms import bisection, newton
import matplotlib.pyplot as plt
import matplotlib
import sympy as sp
import os
import uuid

app = Flask(__name__)
matplotlib.use('Agg')
MY_DIR = r"C:\Users\ASUS\HarbourSpace\module8-math_for_programming\web_app_root_finding"
os.chdir(MY_DIR)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    image_path = None

    if request.method == "POST":
        user_func = request.form["function"]
        interval_a = float(request.form["interval_a"])
        interval_b = float(request.form["interval_b"])
        precision = float(request.form["precision"])

        bisection_result = bisection([interval_a, interval_b], precision, user_func)
        newton_result = newton([interval_a, interval_b], precision, user_func)

        if None in newton_result:
            result = False
        else:
            result = [bisection_result, newton_result]
            image_path = plot_converge(bisection_result[2], newton_result[2])

    return render_template("index.html", result=result, image_path=image_path)

def plot_converge(bisection_errors, newton_errors):
    plt.figure(figsize=(10, 6))
    plt.plot(bisection_errors, label="Bisection Method", marker='o')
    plt.plot(newton_errors, label="Newton's Method", marker='o')
    plt.yscale('log')
    plt.xlabel("Iterations")
    plt.ylabel("Error (log scale)")
    plt.title("Convergency Rate")
    plt.legend()
    plt.grid(True)

    image_path = f'static/images/convergence_plot.png'
    plt.savefig(image_path)
    plt.close()
    return image_path

if __name__ == "__main__":
    app.run(debug=True)

# End of file
