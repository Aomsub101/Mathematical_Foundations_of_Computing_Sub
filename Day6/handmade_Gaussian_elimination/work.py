import random as r

N = [5, 10, 20]
MAX_SOL = r.choice(N)

X = [r.randint(1, 10) for _ in range(MAX_SOL)]
A = [[r.randint(-10, 10) for _ in range(MAX_SOL)] for _ in range(MAX_SOL)]
B = []
for i in range(MAX_SOL):
    res = 0
    for j in range(MAX_SOL):
        res += A[i][j]*X[j]
    B.append(res)

# Hilbert sometin
H = [[1/(i+j+1) for j in range(MAX_SOL)] for i in range(MAX_SOL)]

H_B = []
for i in range(MAX_SOL):
    res = 0
    for j in range(MAX_SOL):
        res += H[i][j]*X[j]
    H_B.append(res)

def gaussian_elimination(A, B, max_sol):
    for i in range(max_sol):
        if A[i][i] == 0:
            for swap_row in range(i, max_sol):
                if A[swap_row][i] != 0:
                    A[i], A[swap_row] = A[swap_row], A[i]
                    B[i], B[swap_row] = B[swap_row], B[i]
                    break
        for j in range(i+1, max_sol):
            factor = A[j][i]/ A[i][i]
            for k in range(max_sol):
                A[j][k] -= factor * A[i][k]
            B[j] -= factor * B[i]
    return A, B

def backward_substitution(A, B, max_sol):
    res = [0] * max_sol
    for i in range(max_sol-1, -1, -1):
        sum_ax = 0
        for j in range(i+1, max_sol):
            sum_ax += A[i][j] * res[j]
        res[i] = (B[i] - sum_ax) / A[i][i]
    return res

def calculate_residue(A, B, X, max_sol):
    A_X = []
    for i in range(max_sol):
        res = 0
        for j in range(max_sol):
            res += A[i][j] * X[j]
        A_X.append(res)
    residue = [A_X[i] - B[i] for i in range(max_sol)]
    return residue


print(f"///////// SIZE IS : {MAX_SOL} /////////")
print("\n******** Normal Matrix ********")
# print("matrix is:")
# for row in A:
#     print(row)
# print(f"B is {B}")

new_A, new_B = gaussian_elimination(A, B, MAX_SOL)

# print("matrix after elimination is:")
# for row in new_A:
#     print(row)
# print(f"B is {new_B}")

normal_answer = backward_substitution(new_A, new_B, MAX_SOL)
normal_residue = calculate_residue(A, B, normal_answer, MAX_SOL)
round_answer = [round(ans) for ans in normal_answer]
print(f"Round answer is: {round_answer}")
print(f"Correct answer is: {X}")
print(f"Check answer: {round_answer == X}")
print(f"Normal_residue is: {normal_residue}")

print("********************************")

print("\n******** Hilbert Matrix ********")
# print("Hilbert matrix is:")
# for row in H:
#     print(row)
# print(f"B is {B}")

new_H, new_H_B = gaussian_elimination(H, H_B, MAX_SOL)

# print("Hilbert matrix after elimination is:")
# for row in new_H:
#     print(row)
# print(f"B is {H_B}")

Hil_ans = backward_substitution(new_H, new_H_B, MAX_SOL)
Hil_residue = calculate_residue(H, H_B, Hil_ans, MAX_SOL)
Hil_round_ans = [round(ans) for ans in Hil_ans]
print(f"Round answer is: {Hil_round_ans}")
print(f"Correct answer is: {X}")
print(f"Check answer: {Hil_round_ans == X}")
print(f"Hilbert_residue is: {Hil_residue}")

print("********************************")
# End of file
