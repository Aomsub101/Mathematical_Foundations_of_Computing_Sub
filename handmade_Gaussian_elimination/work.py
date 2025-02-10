import random as r

MAX_SOL = 5
num_sol = r.randint(2, MAX_SOL)

X = [r.randint(-10, 10) for _ in range(num_sol)]
A = [[r.randint(-10, 10) for _ in range(num_sol)] for _ in range(num_sol)]

B = []
for i in range(num_sol):
    res = 0
    for j in range(num_sol):
        res += A[i][j]*X[j]
    B.append(res)


print(X)
print(A)
print(B)

# End of file
