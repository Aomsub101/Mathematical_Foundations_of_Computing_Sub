import random as r

MAX_SOL = 5
num_sol = 2# r.randint(2, MAX_SOL)

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
                A[i], A[swap_row] = A[swap_row], A[i]  # Swap rows in A
                B[i], B[swap_row] = B[swap_row], B[i]  # Swap elements in B
                break
    for j in range(i+1, num_sol):
        tmp1, tmp2 = A[j][i], A[i][i]
        for k in range(num_sol):
            A[j][k] -= int(tmp1 / tmp2 * A[i][k])
        B[j] -= int(tmp1 / tmp2 * B[i])

print("Matrix after elimination is:")
for row in A:
    print(row)
print(f"B is {B}")

answer = [0] * num_sol
for i in range(num_sol-1, -1, -1):
    sum_ax = 0
    for j in range(i, num_sol):
        sum_ax += A[i][j] * answer[j]
    answer[i] = (B[i] - sum_ax) / A[i][i]

print(f"Solution is: {answer}")
print(f"Check answer: {answer == X}")
