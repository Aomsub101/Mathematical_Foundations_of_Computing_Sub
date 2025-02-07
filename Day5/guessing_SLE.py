"""
Guessing Game Yay!
"""

import random as r

N = 2
A = [[r.randint(1, 5),r.randint(1, 5)] for _ in range(N)]
real_solution = [r.randint(1, 5) for _ in range(N)]

b = [
    A[0][0] * real_solution[0] + A[0][1] * real_solution[1],
    A[1][0] * real_solution[0] + A[1][1] * real_solution[1]
]

print("""
Welcome to guessing game!
Pls guess the answer of this linear equation
""")
print(f"Matrix is {A}\nRight hand side is {b}")

solved = False
while not solved:
    x = []
    for i in range(N):
        x.append(int(input(f"Pls enter x{i}:")))
    # print(f"Your guess is {x}!")
    test1 = A[0][0] * x[0] + A[0][1] * x[1]
    test2 = A[1][0] * x[0] + A[1][1] * x[1]
    # print(test1, test2)
    if test1 == b[0] and test2 == b[1]:
        print('Correct!')
        solved = True
    else:
        print(f"Incorrect, try again. \nError1: {test1-b[0]}\nError2: {test2-b[1]}")
    
# End of file
