import numpy as np
import matplotlib.pyplot as plt
import random as r
import math

a = -20
b = 20
m = 5

def f(x):
    return np.sin(x)

def interpolate(x):
    y = 0
    for j in range(m):
        y += solve_matrix[j] * (x**j)
    return y



points_x = [r.uniform(a, b) for _ in range(m)]
y = []
for x in points_x:
    y.append(f(x))

print("points_x:", points_x)
print("real_answer:", y)

interp_x = np.linspace(a, b, 100)
interp_y = interpolate(interp_x)
real_graph = f(interp_x)

plt.figure(figsize=(10, 6))
plt.plot(points_x, y, 'ro', label='Real Points')
plt.plot(interp_x, real_graph, label='Real Function')
plt.plot(interp_x, interp_y, '--', label='Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Comparison of Real Function and Interpolation')
plt.legend()
plt.grid(True)
plt.show()

# End of file

