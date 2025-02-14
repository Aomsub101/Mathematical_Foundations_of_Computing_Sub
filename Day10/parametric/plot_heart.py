import numpy as np
import matplotlib.pyplot as plt

def y_heart(t):
    return 13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)

def x_heart(t):
    return 16 * np.sin(t)**3

theta = np.linspace(0, 2 * np.pi, 500)
x = x_heart(theta)
y = y_heart(theta)

plt.figure(figsize=(6, 6))
plt.plot(x, y, label="Heart Curve", color='pink')
plt.title(f'Heart')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()

# End of file
