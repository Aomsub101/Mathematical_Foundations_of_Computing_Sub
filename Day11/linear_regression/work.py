import numpy as np
import matplotlib.pyplot as plt

c0 = 1
c1 = 1

a = -10
b = 10
n = 100

def f(x):
    return 2*x + 1

def linear_regression(x, y, n):
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x2 = np.sum(x**2)
    sum_xy = np.sum(x*y)
    m = (n*sum_xy - sum_x*sum_y) / (n*sum_x2 - sum_x**2)
    c = (sum_y - m*sum_x) / n
    return m, c

x = np.linspace(a, b, n)
y = f(x) + np.random.normal(-2, 2, n)

m, c = linear_regression(x, y, n)
y_pred = m*x + c

plt.figure(figsize=(8, 6))
plt.plot(x, y, 'o', label='Data points')
plt.plot(x, y_pred, label='Linear Regression', color='red')
plt.title('Linear Regression')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
# End of file
