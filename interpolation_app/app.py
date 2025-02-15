from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import os

app = Flask(__name__)
MY_DIR = r"C:\Users\ASUS\HarbourSpace\module8-math_for_programming\interpolation_app"

def parse_file(file):
    data = np.genfromtxt(file, delimiter=',', encoding='utf-8-sig')
    x = data[:, 0]
    y = data[:, 1]
    return x, y

def lagrange_interpolation(x_points, y_points):
    n = len(x_points)
    polynomial = 0
    x = sp.symbols('x')

    for i in range(n):
        L_i = y_points[i]
        for j in range(n):
            if j != i:
                L_i *= (x - x_points[j]) / (x_points[i] - x_points[j])
        polynomial += L_i
    return sp.lambdify(x, polynomial, 'numpy')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        x = y = a = b = degree = None
        methods = request.form.getlist('interp_method')
        eval_point = request.form.get('eval_point')
        if eval_point or eval_point:
            eval_point = float(eval_point)
        file = request.files.get('file')
        results = {}
        evaluation = {}

        if file:
            file_path = os.path.join("static", "uploads", file.filename)
            save_path = os.path.join(MY_DIR, file_path)

            file.save(save_path)
            x, y = parse_file(save_path)
            print(x, y)
            a, b = min(x), max(x)
            degree = len(x) - 1
        else:
            a = float(request.form['interval_a'])
            b = float(request.form['interval_b'])
            degree = int(request.form['degree'])
            x = np.linspace(a, b, degree + 1)

            expr = sp.sympify(request.form['function'])
            f = sp.lambdify('x', expr, 'numpy')
            y = f(x)

        plt.figure(figsize=(10, 6))
        plt.plot(x, y, 'ko', label='Original points')

        if 'lagrange' in methods:
            lagrange_poly = lagrange_interpolation(x, y)
            x_dense = np.linspace(a, b, 100)
            plt.plot(x_dense, lagrange_poly(x_dense), '--', label='Lagrange')
            # results['Lagrange'] = laprange_poly

            if eval_point or eval_point == 0:
                evaluation['Lagrange Polynomial'] = f'f({eval_point}) = {lagrange_poly(eval_point):.4f}'

        if 'parametric' in methods:
            t = np.arange(len(x))
            poly_x = np.polyfit(t, x, len(t)-1)
            poly_y = np.polyfit(t, y, len(t)-1)
            t_dense = np.linspace(0, t[-1], 100)
            plt.plot(
                np.polyval(poly_x, t_dense),
                np.polyval(poly_y, t_dense),
                label='Parametric'
            )
            # results['Parametric'] = (poly_x, poly_y)

            if eval_point or eval_point == 0:
                x_val = np.polyval(poly_x, eval_point)
                y_val = np.polyval(poly_y, eval_point)
                evaluation['Parametric'] = f'x({eval_point}) = {x_val:.4f}\ny({eval_point}) = {y_val:.4f}'

        if 'polynomial_sle' in methods:
            vander = np.vander(x, degree+1)
            coeffs = np.linalg.solve(vander, y)
            poly_sle = np.poly1d(coeffs)
            x_dense = np.linspace(a, b, 100)
            plt.plot(x_dense, poly_sle(x_dense), label='SLE Polynomial')
            # results['SLE'] = poly_sle

            if eval_point or eval_point == 0:
                evaluation['SLE Polynomial'] = f'f({eval_point}) = {poly_sle(eval_point):.4f}'

        plt.legend()
        plt.grid(True)
        plt.title('Interpolation Comparison')

        img_path = os.path.join("static", "images", "plot.png")
        save_path = os.path.join(MY_DIR, img_path)

        os.makedirs(os.path.dirname(save_path), exist_ok=True)  # Ensure dir exists
        plt.savefig(save_path)

        return render_template('index.html',
                                plot_path=img_path.replace("\\", "/"),
                                evaluation=evaluation)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

# End of file
