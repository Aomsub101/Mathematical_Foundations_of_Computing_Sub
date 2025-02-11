import random as r
import math
N = r.randint(2, 10)
ERROR = 1e-8

def generate_hilbert():
    H = [[1/(i+j+1) for j in range(N)] for i in range(N)]
    X = [r.randint(1, 10) for _ in range(N)]
    H_B = []
    for i in range(N):
        res = 0
        for j in range(N):
            res += H[i][j]*X[j]
        H_B.append(res)

    return H, H_B, X

def seidal_algo(A, B, initial_guess):
    current_ans = initial_guess.copy()
    itr = 0
    while True:
        itr += 1
        prev_ans = current_ans.copy()
        for i in range(N):
            sum_ = 0
            for j in range(N):
                if i != j:
                    sum_ += A[i][j] * current_ans[j]
            current_ans[i] = (B[i] - sum_) / A[i][i]

        if max(abs(current_ans[i] - prev_ans[i]) for i in range(N)) < ERROR:
            return current_ans, itr

print("****** Hilbert *****")
H, H_B, X = generate_hilbert()

print(f"matrix is :{H}")
print(f"B is :{H_B}")

initial_guess = [0] * N
answer, itr = seidal_algo(H, H_B, initial_guess)

print(f"real answer is :{X}")
print(f"final answer is :{answer}")
print(f"Total iterations: {itr+1}")

s = 0
d = 0
for i in range(N):
    s += (answer[i] - X[i])**2
    d += (answer[i] - X[i])
d /= N
print(f"Error is: {math.sqrt(s)}")
print(f"Distance to real answer: {d}")
# End of file
