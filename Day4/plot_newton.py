import random as r
import math
import matplotlib.pyplot as plt

prev_x = 5
eps = 1e-10

def f(x):
    return x**2 - 5*x + 4

def f_prime(x):
    return 2*x - 5

i = 0
x_values = []

while True:
    print(f"{i}-th iteration: x = {prev_x}")
    x = prev_x - f(prev_x) / f_prime(prev_x)
    x_values.append(x)
    if abs(x - prev_x) < eps:
        break
    i += 1
    prev_x = x

print(f"It took {i} iterations to find root in precision of {eps}")

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(range(len(x_values)), x_values, marker='o', linestyle='-', color='b', label='x values')
plt.axhline(0, color='gray', linestyle='--', linewidth=0.5)  # Add a horizontal line at y=0
plt.xlabel('Iteration')
plt.ylabel('error')
plt.title('Newton-Raphson Method Iterations')
plt.legend()
plt.grid(True)
plt.show()
