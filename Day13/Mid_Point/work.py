import numpy as np
import matplotlib.pyplot as plt
import random as r
import math

n = 5
x_mid = r.randint(0, 5)
y_mid = r.randint(0, 5)
x_cord = [x_mid + r.choice([r.uniform(-5, -1), r.uniform(1, 5)]) for _ in range(n)]
y_cord = [y_mid + r.choice([r.uniform(-5, -1), r.uniform(1, 5)]) for _ in range(n)]
eps = 1.5

def plot_circle(x, y, r, ax):
    """Plots a semi-transparent circle at (x, y) with radius r."""
    circle = plt.Circle((x, y), r, color='b', alpha=0.5, fill=False)  # Transparent outline
    ax.add_patch(circle)

d = []
d1 = math.sqrt((x_cord[0] - x_mid) ** 2 + (y_cord[0] - y_mid) ** 2)
radii = [d1]
for i in range(1, n):
    di = math.sqrt((x_cord[i] - x_mid) ** 2 + (y_cord[i] - y_mid) ** 2)
    res = - d1 ** 2 + di ** 2 + x_cord[0] ** 2 + y_cord[0] ** 2 - x_cord[i] ** 2 - y_cord[i] ** 2
    res += r.choice([eps, -eps])
    d.append(res)
    radii.append(di)  # Store radius for each data point

A = [[2 * x_cord[0] - 2 * x_cord[i], 2 * y_cord[0] - 2 * y_cord[i]] for i in range(1, n)]
b = d

A = np.array(A)
b = np.array(b)

x = np.linalg.solve(A.T @ A, A.T @ b)

print(f"Mid points: {x}")
print(f"Original Mid points: ({x_mid}, {y_mid})")

fig, ax = plt.subplots(figsize=(8, 6))
ax.set_aspect('equal')  # Keep the aspect ratio square

# Plot original and calculated midpoint
ax.plot(x_mid, y_mid, 'ro', label='Original Mid Point')
ax.plot(x_cord, y_cord, 'bo', label='Data Points')
ax.plot(x[0], x[1], 'g^', label='Calculated Mid Point')

# Plot circles
for i in range(n):
    plot_circle(x_cord[i], y_cord[i], radii[i], ax)

plt.title('Intersection of Circles at Midpoint')
plt.legend()
plt.show()

# End of file
