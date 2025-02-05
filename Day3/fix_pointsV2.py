import random as r
import math

epsilon = 1e-16

prev_x = r.uniform(1, 3)

def g1(x: float) -> float:
    return x**2 - 2

def g2(x: float) -> float:
    return math.sqrt(x+2)

def g3(x: float) -> float:
    return (x+2)/x

def g4(x: float) -> float:
    return -(x**2 - x - 2)/6 + x

i = 0
print(f"Starting point: {prev_x}")
while True:
    print(f"{i}-th iteration: x = {prev_x}")
    x = g4(prev_x)
    if abs(x - prev_x) < epsilon:
        break
    i += 1
    prev_x = x

print(f"Total iteration: {i}")
# End of file
