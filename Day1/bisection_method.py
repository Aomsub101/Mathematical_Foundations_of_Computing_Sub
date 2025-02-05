import math

interval = [1, 4]
a = interval[0]
b = interval[1]
m = 0
eps = 0.1
approx_iteration = math.log2(abs((b-a)/eps))

def f(x: float) -> float:
    return math.sin(x)

itr = 0

while True:
    itr += 1
    f_a = f(a)
    f_b = f(b)
    if f_a * f_b < 0:
        m = (a + b)/2
        f_m = f(m)
        if f_a * f_m < 0:
            b = m
        else:
            a = m
        if b - a < eps:
            break
    else:
        print(f"No root in interval: {interval}")
        break

print(f"approx_iteration: {approx_iteration}")
print(f"actual iteration: {itr}")
print(f"root: {m}")
# end of file
