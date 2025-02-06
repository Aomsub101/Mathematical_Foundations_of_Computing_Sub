import random as r
import math

prev_x = 500000
eps = 1e-10

def f(x):
    return x**2 - 5*x + 4

def f_prime(x):
    return 2*x - 5

i = 0
while True:
    print(f"{i}-th iteration: x = {prev_x}")
    x = prev_x - f(prev_x)/f_prime(prev_x)
    if abs(x - prev_x) < eps:
        break
    i += 1
    prev_x = x

print(f"It took {i} iterations to find root in precision of {eps}")
# End of file