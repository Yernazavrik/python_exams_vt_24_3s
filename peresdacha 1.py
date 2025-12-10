import math

def stepen(x,y):
    if y >= 1:
        return x*stepen(x, y-1)
    else:
        return 1
    
def fact(k):
    if k <= 1:
        return 1
    return k * fact(k - 1)

def PS(x, y, n):
    if n <= 0:
        return 0, 1  

    prev_sum, prev_prod = PS(x, y, n - 1)
    
    term = stepen(x, y) / (math.sqrt(fact(y)) + math.sqrt(fact(x)))
    
    new_sum = prev_sum + term
    new_prod = prev_prod * term
    
    return new_sum, new_prod

x = int(input("Введите x: "))
y = int(input("Введите y: "))
n = int(input("Введите n: "))

result = PS(x, y, n)
print(result)