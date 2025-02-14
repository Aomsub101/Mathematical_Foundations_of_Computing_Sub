import numpy as np
import matplotlib.pyplot as plt
import random as r

radius = r.randint(1, 10)
center = (0, 0)

def x_circle(t):
    return radius * np.cos(t)

def y_circle(t):
    return radius * np.sin(t)

theta = np.linspace(0, 2 * np.pi, 500)
parametric_x = x_circle(theta)
parametric_y = y_circle(theta)

plt.figure(figsize=(6, 6))
plt.plot(parametric_x, parametric_y)
plt.title(f'Circle with radius {radius}')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()

# End of file
