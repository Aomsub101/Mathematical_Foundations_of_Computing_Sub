import numpy as np
import matplotlib.pyplot as plt
import random as r
import math

a = -20
b = 20
m = 5

def f(x):
    return np.sin(x)

def get_matrix(points_x):
    matrix = []
    for i in range(m):
        row = []
        for j in range(m):
            row.append(points_x[i]**j)
        matrix.append(row)
    return matrix

def interpolate(x):
    y = 0
    for j in range(m):
        y += solve_matrix[j] * (x**j)
    return y

# this is the real solution and function
points_x = [r.uniform(a, b) for _ in range(m)]
real_answer = []
for x in points_x:
    real_answer.append(f(x))
###########################

# we are generating a matrix here
matrix = get_matrix(points_x)

# we solve the matrix here
solve_matrix = np.linalg.solve(matrix, real_answer)

print("points_x:", points_x)
print("real_answer:", real_answer)
print("matrix:", matrix)
print("Solution:", solve_matrix)

interp_x = np.linspace(a, b, 100)
interp_y = interpolate(interp_x)
real_graph = f(interp_x)

plt.figure(figsize=(10, 6))
plt.plot(points_x, real_answer, 'ro', label='Real Points')
plt.plot(interp_x, real_graph, label='Real Function')
plt.plot(interp_x, interp_y, '--', label='Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Comparison of Real Function and Interpolation')
plt.legend()
plt.grid(True)
plt.show()

# End of file

