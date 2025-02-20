import numpy as np
import matplotlib.pyplot as plt

def g(x, c):
    n = len(c)
    res = c[0]
    for i in range(1, n):
        res += c[i] * x ** i
    return res

def Phi(c, x, y):
    return 0.5 * np.linalg.norm(y - g(x, c)) ** 2

def d_Phi_by_d_ci(c, x, y, i):
    return np.sum((g(x, c) - y)* x ** i)

n = 100

x = np.linspace(0, 10, n)
y = -x**3 + 2*x ** 2 + 30*x - 10
y_noisy = y + np.random.normal(0, 15, n)

c = np.array([1.0, 1.0, 1.0, 1.0])
max_iters = 1000000
alpha = 0.0000001
eps = 1e-6
it = 0
for i in range(max_iters):
    c_prev = c.copy()
    print(c)
    for j in range(c.shape[0]): # shape[0] is number of row
        c[j] -= alpha * d_Phi_by_d_ci(c, x, y_noisy, j)
    if np.linalg.norm(c - c_prev) < eps:
        break
    it += 1

print(f"iterations: {it}")
x_fine = np.linspace(0, 10, 400)
y_fine = g(x_fine, c)

plt.scatter(x, y_noisy, color="red", label="Data points")
plt.plot(x_fine, y_fine, label="regression line")
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()

#End of file
