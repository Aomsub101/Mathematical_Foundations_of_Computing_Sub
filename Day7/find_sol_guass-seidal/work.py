import random as r
import math
N = r.randint(2, 20)
ERROR = 1e-6
MAX_ITR = 10000

def diagonal_dominance(A):
    for i in range(N):
        sum_ = 0
        for j in range(N):
            if j != i:
                sum_ += abs(A[i][j])
        if abs(A[i][i]) <= sum_:
            A[i][i] += sum_+ 1
            A[i][i] *= sum_ + 1

    return A

def generate_matrix():
    A = [[r.randint(-10, 10) for _ in range(N)] for _ in range(N)]
    X = [r.randint(1, 10) for _ in range(N)]
    c_A = diagonal_dominance(A)

    B = []
    for i in range(N):
        res = 0
        for j in range(N):
            res += c_A[i][j]*X[j]
        B.append(res)

    return c_A, B, X

def seidal_algo(A, B, initial_guess, ERROR, MAX_ITR):
    current_ans = initial_guess.copy()
    for itr in range(MAX_ITR):
        prev_ans = current_ans.copy()
        for i in range(N):
            sum_ = 0
            for j in range(N):
                if i != j:
                    sum_ += A[i][j] * prev_ans[j]
            prev_ans[i] = (B[i] - sum_) / A[i][i]
        # print(f"x{itr}: {prev_ans}")
        if max(abs(current_ans[i] - prev_ans[i]) for i in range(N)) < ERROR:
            return current_ans, itr
        current_ans = prev_ans
    print("Diverged!")
    print("Max iteration reach!")
    return current_ans, itr
A, B, X = generate_matrix()

print(f"matrix is :{A}")
print(f"B is :{B}")

initial_guess = [0] * N
answer, itr = seidal_algo(A, B, initial_guess, ERROR, MAX_ITR)

print(f"real answer is :{X}")
print(f"final answer is :{answer}")
print(f"Total iterations: {itr}")

s = 0
d = 0
for i in range(N):
    s += (answer[i] - X[i])**2
    d += (answer[i] - X[i])
d /= N
print(f"Error is: {math.sqrt(s)}")
print(f"Distance to real answer: {d}")

# End of file
