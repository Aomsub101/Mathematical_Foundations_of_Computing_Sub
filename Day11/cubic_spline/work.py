import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange, CubicSpline

def f(x):
    return 1 / (1 + 25 * x**2)

n = 10
x_interp = np.linspace(-1, 1, n)  # Chebyshev nodes can also be used for better results
y_interp = f(x_interp)

lagrange_poly = lagrange(x_interp, y_interp)

cubic_spline = CubicSpline(x_interp, y_interp, bc_type='natural')

x_plot = np.linspace(-1, 1, 500)
y_true = f(x_plot)
y_lagrange = lagrange_poly(x_plot)
y_spline = cubic_spline(x_plot)

plt.figure(figsize=(8, 6))
plt.plot(x_plot, y_true, 'k', color="blue", label="Original function f(x)", linewidth=2)
plt.plot(x_plot, y_lagrange, 'r--', color="red", label="Lagrange Interpolation")
plt.plot(x_plot, y_spline, 'b-.', color="pink", label="Cubic Spline Interpolation")
plt.scatter(x_interp, y_interp, c='black', marker='o', label="Interpolation points")
plt.legend()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.ylim(min(x_interp) - 0.2, max(x_interp) + 1)
plt.title("Function Interpolation using Lagrange and Cubic Spline")
plt.grid()
plt.show()

# End of file
