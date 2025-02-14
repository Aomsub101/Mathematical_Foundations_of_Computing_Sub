import numpy as np
import matplotlib.pyplot as plt

x = np.loadtxt('Day10/contour/x.csv')
y = np.loadtxt('Day10/contour/y.csv')

n_points = 1900
t_new = np.linspace(0, n_points - 1, 300)
x_poly = np.polyval(x, t_new)
y_poly = np.polyval(y, t_new)

plt.figure(figsize=(6, 6))
plt.plot(x_poly, y_poly)
plt.show()


# End of file
