import random as r
import math
import matplotlib.pyplot as plt
import os

N = r.randint(20,100)
ERROR = 1e-6
MAX_ITR = 10000
CUR_DIR = os.getcwd()

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

def jacobi_algo(A, B, initial_guess, X):
    current_ans = initial_guess.copy()
    errors = []
    for itr in range(MAX_ITR):
        prev_ans = current_ans.copy()
        for i in range(N):
            sum_ = 0
            for j in range(N):
                if i != j:
                    sum_ += A[i][j] * current_ans[j]
            prev_ans[i] = (B[i] - sum_) / A[i][i]

        err = 0
        for i in range(N):
            err += (prev_ans[i] - X[i])**2
        errors.append(math.sqrt(err))

        if max(abs(prev_ans[i] - current_ans[i]) for i in range(N)) < ERROR:
            itr += 1
            return prev_ans, itr, errors
        current_ans = prev_ans

def seidal_algo(A, B, initial_guess, X):
    current_ans = initial_guess.copy()
    errors = []
    for itr in range(MAX_ITR):
        prev_ans = current_ans.copy()
        for i in range(N):
            sum_ = 0
            for j in range(N):
                if i != j:
                    sum_ += A[i][j] * prev_ans[j]
            prev_ans[i] = (B[i] - sum_) / A[i][i]

        err = 0
        for i in range(N):
            err += (prev_ans[i] - X[i])**2
        errors.append(math.sqrt(err))

        if max(abs(current_ans[i] - prev_ans[i]) for i in range(N)) < ERROR:
            itr += 1
            return current_ans, itr, errors
        current_ans = prev_ans
    print("Diverged!")
    print("Max iteration reach!")
    return current_ans, itr

def error_plot(error_seidal, error_jacobi, itr_seidal, itr_jacobi):
    itr_jacobi = [i for i in range(itr_jacobi)]
    itr_seidal = [i for i in range(itr_seidal)]

    plt.plot(itr_seidal, error_seidal, label="seidal's error")
    plt.plot(itr_jacobi, error_jacobi, label="jacobi's error")
    plt.xlabel("Iterations")
    plt.ylabel("Error")
    plt.grid(True)
    plt.legend()
    dir_ = f'{CUR_DIR}\Day7\compare_seidal_jacobi_plot\images\plot.png'
    plt.savefig(dir_)
    plt.show()

def main():
    A, B, X = generate_matrix()
    print(f"/////  SIZE: {N}  /////")
    print(f"matrix is :{A}")
    print(f"B is :{B}")

    initial_guess = B
    answer_seidal, itr_seidal, error_seidal = seidal_algo(A, B, initial_guess, X)
    answer_jacobi, itr_jacobi, error_jacobi = jacobi_algo(A, B, initial_guess, X)

    print(f"real answer is :{X}")
    print(f"\nJacobi's sol: {answer_jacobi}")
    print(f"Jacobi's iterations: {itr_jacobi}")
    print(f"Jacobi's error: {error_jacobi[-1]}")

    print("*"*20)

    print(f"\nSeidal's sol: {answer_seidal}")
    print(f"Seidal's iterations: {itr_seidal}")
    print(f"Seidal's error: {math.sqrt(error_seidal[-1])}")

    error_plot(error_seidal, error_jacobi, itr_seidal, itr_jacobi)

    # print(CUR_DIR)
main()
# End of file
