import math

def f(i, n, x):
    if i > n:
        return 0
    return x**i / math.exp(i*i)+(i*i) + f(i + 1, n, x)

n = 6
x = 2
print(f(1, n, x))