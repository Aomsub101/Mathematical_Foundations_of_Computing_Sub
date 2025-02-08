from sympy import symbols, sympify
import random as r

x = symbols('x')

def bisection(interval, precision, f, itr=0, errors=None):
    if errors is None:
        errors = []

    f = sympify(f)
    left, right = interval
    if abs(left - right) <= precision:
        root = (left + right) / 2
        return [root, itr, errors]

    mid = (left + right) / 2
    error = abs(right - left) / 2
    errors.append(error)
    itr += 1

    if f.subs(x, left) * f.subs(x, mid) < 0:
        return bisection([left, mid], precision, f, itr, errors)
    else:
        return bisection([mid, right], precision, f, itr, errors)

def newton(interval, precision, f):
    f = sympify(f)
    f_prime = f.diff('x')
    left, right = interval
    root = r.uniform(left, right)
    errors = []
    itr = 0

    while True:
        prev_root = root
        root = prev_root - f.subs(x, prev_root) / f_prime.subs(x, prev_root)
        error = abs(root - prev_root)
        errors.append(error)
        itr += 1
        if error < precision:
            break

    if left <= root <= right:
        return [root, itr, errors]
    return None, None, None

# End of file
