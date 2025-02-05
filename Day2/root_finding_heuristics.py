import time
import numpy as np
import matplotlib.pyplot as plt

interval = [-3,2]
EPS = 1e-10
DELTA = 1e-6
roots = []

# approx_iteration = math.log2(abs((b-a)/EPS))
def f(x):
    return x**4 + 3*(x**3) + x**2 - 2*x - 0.5

def get_root_bisection(a: float, b: float) -> float:
    """
    calculate the root in particular interval
    """
    while f(a) * f(b) < 0:
        mid = (a + b)/2
        if f(a) * f(mid) < 0:
            b = mid
        else:
            a = mid
    return (a + b)/2

def find_root_interval(a: float,b: float) -> None:
    """
    Recursively divided interval in half until finding a root.
    """
    if b - a < DELTA:
        return
    if f(a) * f(b) < 0:
        roots.append(get_root_bisection(a,b))
    else:
        mid = (a+b)/2
        find_root_interval(a,mid)
        find_root_interval(mid,b)

def main():
    start_time = time.time()

    find_root_interval(interval[0],interval[1])

    end_time = time.time()
    plt.show()
    print(f"All roots: {roots}")
    print(f"Total program time: {end_time - start_time}")

if __name__ == '__main__':
    main()

# end of file
