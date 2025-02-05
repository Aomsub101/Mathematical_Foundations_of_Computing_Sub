import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


interval = [0, 5]
EPS = 1e-10
DELTA = 1e-6
roots = []
fig, ax = plt.subplots()

def f(x):
    """
    function
    """
    return x ** 3 - 20

def get_root_bisection(a: float, b: float) -> float:
    """
    calculate the root in particular interval
    """
    # print(a, b)
    points = []
    while f(a) * f(b) < 0:
        if b - a < EPS:
            break
        mid = (a + b)/2
        if f(a) * f(mid) < 0:
            b = mid
        else:
            a = mid
        points.append(mid)
    return points

def main():
    x = np.linspace(interval[0], interval[1], 100)
    y = f(x)
    ax.plot(x, y, color="blue")
    ax.plot(x, np.zeros_like(x), color="black", label="Graph of f(x)")
    ax.set_xlabel('X')
    ax.set_ylabel('f(x)')
    points = get_root_bisection(interval[0], interval[1])
    frames = []

    for itr, point in enumerate(points):
        # print("we are here")
        frame = ax.plot(point, f(point), 'ro', color="red")
        frames.append(frame + [ax.text(0.5, 1.05, f"Iteration {itr}: Midpoint = {point:.6f}",
                                       transform=ax.transAxes, ha="center")])

    ani = animation.ArtistAnimation(fig=fig, artists=frames, interval=400, repeat=False)
    plt.show()

main()

# end of file
