import random as r

MAX_SOL = 5
num_sol = r.randint(2, MAX_SOL)

X = [r.randint(1, 10) for _ in range(num_sol)]
A = [[r.randint(-10, 10) for _ in range(num_sol)] for _ in range(num_sol)]

B = []
for i in range(num_sol):
    res = 0
    for j in range(num_sol):
        res += A[i][j]*X[j]
    B.append(res)

print("Matrix is:")
for row in A:
    print(row)
print(f"B is {B}")

for i in range(num_sol):
    if A[i][i] == 0:
        for swap_row in range(i, num_sol):
            if A[swap_row][i] != 0:
                A[i], A[swap_row] = A[swap_row], A[i]
                B[i], B[swap_row] = B[swap_row], B[i]
                break
    for j in range(i+1, num_sol):
        factor = A[j][i]/ A[i][i]
        for k in range(num_sol):
            A[j][k] -= factor * A[i][k]
        B[j] -= factor * B[i]

print("Matrix after elimination is:")
for row in A:
    print(row)
print(f"B is {B}")

answer = [0] * num_sol
for i in range(num_sol-1, -1, -1):
    sum_ax = 0
    for j in range(i+1, num_sol):
        sum_ax += A[i][j] * answer[j]
    answer[i] = (B[i] - sum_ax) / A[i][i]

print(f"Answer is: {answer}")
answer = [round(ans) for ans in answer]
print(f"Round answer is: {answer}")
print(f"Correct answer is: {X}")
print(f"Check answer: {answer == X}")
