import numpy as np
import matplotlib.pyplot as plt
import random as r

radius = 1
center = (0, 0)
a, b = 0, 2 * np.pi

def x_circle(t):
    return radius * np.cos(t)

def y_circle(t):
    return radius * np.sin(t)

def get_interp_func(t_i, x_vals, y_vals, degree):
    coeff_x = np.polyfit(t_i, x_vals, degree)
    coeff_y = np.polyfit(t_i, y_vals, degree)
    return np.poly1d(coeff_x), np.poly1d(coeff_y)

theta = np.linspace(a, b, 100)
x_original = x_circle(theta)
y_original = y_circle(theta)

n = 5 # m-points
t_i = np.linspace(a, b, n)

x_vals = x_circle(t_i)
y_vals = y_circle(t_i)

degree = n-1
poly_x, poly_y = get_interp_func(t_i, x_vals, y_vals, degree)

t_plot = np.linspace(a, b, 100)
interp_x = np.polyval(poly_x, t_plot)
interp_y = np.polyval(poly_y, t_plot)

plt.figure(figsize=(8, 8))
plt.plot(x_vals, y_vals, 'o', label='points')
plt.plot(x_original, y_original, '--', label='Original Circle')
plt.plot(interp_x, interp_y, 'b-', label='Interpolated Points', color='red')
plt.title(f'Circle with radius {radius} and Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()

# End of file