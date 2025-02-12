import numpy as np
import matplotlib.pyplot as plt
import random as r
import os

a = 0
b = 4
m = 5
CUR_DIR = os.getcwd()
CUR_DIR = f"{CUR_DIR}\Day8\interpolation&lagrange\images"

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

points_x = [r.uniform(a, b) for _ in range(m)]
real_answer = []
for x in points_x:
    real_answer.append(f(x))

def get_L(exc, points_x, x):
    res = 1
    for i in range(m):
        if i != exc:
            res *= (x - points_x[i])/(points_x[exc] - points_x[i])

    return res

def lagrange(x):
    res = 0
    for i in range(m):
        L = get_L(i,points_x,x)
        res += L * real_answer[i]
    return res

matrix = get_matrix(points_x)

solve_matrix = np.linalg.solve(matrix, real_answer)

print("points_x:", points_x)
print("real_answer:", real_answer)
print("matrix:", matrix)
print("Solution:", solve_matrix)

interp_x = np.linspace(a, b, 100)
interp_y = interpolate(interp_x)
lagrange_y = lagrange(interp_x)
real_graph = f(interp_x)


plt.figure(figsize=(10, 6))
plt.plot(points_x, real_answer, 'ro', label='Real Points')
plt.plot(interp_x, real_graph, label='Real Function')
plt.plot(interp_x, lagrange_y, label='Lagrange Function')
plt.plot(interp_x, interp_y, '--', label='Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'Comparison of Real Function and Interpolation f(x) = sin(x) m:{m} points')
plt.legend()
plt.grid(True)

img_name = "\plot_sinX.png"
plt.savefig(CUR_DIR+img_name)
plt.show()

# End of file

