import numpy as np
import matplotlib.pyplot as plt

# function c0 + c1*np.cos(x) + c2*np.sin(x) + c3*x + c4*(x**2) + c5*np.log(x)
def f(x, c):
    return c[0] + c[1]*np.cos(x) + c[2]*np.sin(x) + c[3]*x + c[4]*(x**2) + c[5]*np.log(x)

data = np.genfromtxt('Day12/approx_func_linear_reg/data.csv', delimiter=',')
points_x = data[:, 0]
points_y = data[:, 1]

def make_func(x, y):
    n = len(x)
    A = np.zeros((n, 6))
    b = np.zeros(n)
    for i in range(n):
        A[i] = [1, np.cos(x[i]), np.sin(x[i]), x[i], x[i]**2, np.log(x[i])]
        b[i] = y[i]
    return A, b

A, b = make_func(points_x, points_y)

c = np.linalg.solve(A.T@A, A.T@b)

# print(A)
# print(b)
print(f"Coefficiented: {c}")

x_plot = np.linspace(min(points_x)-2, max(points_x)+2, 500)
y_plot = f(x_plot, c)

plt.figure(figsize=(8, 6))
plt.plot(points_x, points_y, 'o', label='Data points')
plt.plot(x_plot, y_plot, label='Approximation function')
plt.title('Approximation function')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()


# Coefficiented: [ 1.16082826 11.97684257 29.98667922 -0.15430161  1.01638063  5.12242519]
# End of file
