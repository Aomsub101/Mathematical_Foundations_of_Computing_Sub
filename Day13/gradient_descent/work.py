import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**2

def f_prime(x):
    return 2*x

x0 = 3
eps = 1e-10
alpha = 0.1
x_vals = []
it = 0

for i in range(1000):
    x_vals.append(x0)
    it += 1
    x1 = x0 - alpha*f_prime(x0)
    if abs(x1 - x0) < eps:
        break
    x0 = x1

print(f"total iterations: {it}")
print(f"Minimum value of x: {x0}")

x = np.linspace(-5, 5, 100)
plt.figure(figsize=(8, 6))
plt.plot(x, f(x), label='f(x) = x^2')
plt.plot(x_vals, [f(x) for x in x_vals], 'o', label='Gradient Descent')
plt.legend()
plt.grid(True)
plt.show()

# End of file
