from decimal import Decimal

N = 10000000
res = Decimal(10.0)
x = Decimal(0.0)

h = res/Decimal(N)

for i in range(N):
    x += h

print(x)
print(x == res)
print(f"{x - res}")
