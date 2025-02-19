import numpy as np
import matplotlib.pyplot as plt
import random as r

data = np.genfromtxt('Day13/Mid_Point/multilateration-data.csv', delimiter=',')
x_cord = data[:, 0]
y_cord = data[:, 1]
d = data[:, 2]
n = len(x_cord)
d1 = d[0]
b = []

for i in range(1, n):
    res = -d1 ** 2 + d[i] ** 2 + x_cord[0] ** 2 + y_cord[0] ** 2 - x_cord[i] ** 2 - y_cord[i] ** 2
    b.append(res)
 
A = [[2 * x_cord[0] - 2 * x_cord[i], 2 * y_cord[0] - 2 * y_cord[i]] for i in range(1, n)]

A = np.array(A)
b = np.array(b)

x = np.linalg.solve(A.T @ A, A.T @ b)

print(f"Mid points: {x}")

fig, ax = plt.subplots(figsize=(8, 6))

ax.plot(x_cord, y_cord, 'bo', label='Data Points')
ax.plot(x[0], x[1], 'g^', label=f'Calculated Mid Point x:{x[0]}, y:{x[1]}')

plt.title('Find Midpoint')
plt.legend()
plt.show()

# End of file
