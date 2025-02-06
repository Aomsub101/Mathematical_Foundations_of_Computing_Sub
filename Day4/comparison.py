import matplotlib.pyplot as plt
import random as r

eps = 1e-5

x_bisc = []
x_fixp = []
x_newton = []

interval = [3, 10]
a = interval[0]
b = interval[1]
x_n = r.uniform(a,b)
x_fp = r.uniform(a,b)

def f(x):
    return x**2 - 5*x + 4

def f_prime_newton(x):
    return 2*x - 5

def fix_point(x):
    return -(x**2 - 5*x + 4) / 6 + x

# Bisection method
while True:
    m = (a + b) / 2
    if abs(b - a) < eps:
        break
    f_a, f_m = f(a), f(m)
    if f_a * f_m < 0:
        b = m
    else:
        a = m
    x_bisc.append(abs(m-4))

# Fixed-Point
while True:
    x_new = fix_point(x_fp)
    x_fixp.append(abs(x_new - 4))
    if abs(x_new - x_fp) < eps:
        break
    x_fp = x_new

# Newton
while True:
    x_new = x_n - f(x_n) / f_prime_newton(x_n)
    x_newton.append(abs(x_new - 4))
    if abs(x_new - x_n) < eps:
        break
    x_n = x_new

# Plotting all three methods
plt.figure(figsize=(12, 6))
plt.plot(range(len(x_bisc)), x_bisc, marker='o', linestyle='-', color='r', label='Bisection Method')
plt.plot(range(len(x_fixp)), x_fixp, marker='o', linestyle='-', color='g', label='Fixed-Point Iteration')
plt.plot(range(len(x_newton)), x_newton, marker='o', linestyle='-', color='b', label='Newton-Raphson Method')

# Labels and legend
plt.xlabel('Iteration')
plt.ylabel('error')
plt.yscale('log')
plt.title('Convergence to Root: Bisection vs Fixed-Point vs Newton')
plt.legend()
plt.grid(True)
plt.show()
