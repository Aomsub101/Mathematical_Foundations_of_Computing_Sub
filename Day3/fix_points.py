import random as r
import math
prev_x = r.randint(4,10)

def f(x):
    return math.sqrt(x)

i = 0
while True:
    print(f"{i} x = {prev_x}")
    x = f(prev_x)
    if prev_x == x:
        break
    i += 1
    prev_x = x

# End of file
