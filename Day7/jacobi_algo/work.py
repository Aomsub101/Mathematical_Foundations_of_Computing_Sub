import random as r
import math

N = r.randint(2, 10)
error = 1e-6
max_itr = 500

def diagonal_dominance(A):
    for i in range(N):
        sum_ = 0
        for j in range(N):
            if j != i:
                sum_ += abs(A[i][j])
        if abs(A[i][i]) <= sum_:
            A[i][i] = sum_+ 1

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

def jacobi_algo(A, B, initial_guess, error, max_itr):
    current_ans = initial_guess.copy()
    for itr in range(max_itr):
        new_ans = current_ans.copy()
        for i in range(N):
            sum_ = 0
            for j in range(N):
                if i != j:
                    sum_ += A[i][j] * current_ans[j]
            new_ans[i] = (B[i] - sum_) / A[i][i]
        print(f"x{itr}: {new_ans}")
        if max(abs(new_ans[i] - current_ans[i]) for i in range(N)) < error:
            itr += 1
            return new_ans, itr
        current_ans = new_ans

A, B, X = generate_matrix()

print(f"matrix is :{A}")
print(f"B is :{B}")

initial_guess = B
answer, itr = jacobi_algo(A, B, initial_guess, error, max_itr)

s = 0
for i in range(N):
    s += (answer[i] - X[i])**2

print(f"real answer is :{X}")
print(f"final answer is :{answer}")
print(f"Total iterations: {itr}")
print(math.sqrt(s))

# End of file
