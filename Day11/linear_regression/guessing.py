import numpy as np
import matplotlib.pyplot as plt

def linear_regression(x, y, n):
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x2 = np.sum(x**2)
    sum_xy = np.sum(x*y)
    m = (n*sum_xy - sum_x*sum_y) / (n*sum_x2 - sum_x**2)
    c = (sum_y - m*sum_x) / n
    return m, c

def f(c1,c0, x):
    return c1*x + c0
 

x = np.loadtxt('Day11/linear_regression/x_points.txt', delimiter=',')
y = np.loadtxt('Day11/linear_regression/y_points.txt', delimiter=',')
m = len(x)

c1, c0 = linear_regression(x, y, m)
x_plot = np.linspace(0, 10, 100)
y_plot = f(c1, c0, x_plot)
print(f"y = {c1}x + {c0}")

plt.figure(figsize=(8, 6))
plt.plot(x, y, 'o', label='Data points')
plt.plot(x_plot, y_plot, label='Linear Regression', color='red')
plt.title('Linear Regression')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
# End of file
