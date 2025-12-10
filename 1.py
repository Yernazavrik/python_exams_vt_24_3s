from math import log

def stepen(x,i):
    if i >= 1:
        return x*stepen(x, i-1)
    else:
        return 1

def S(n,x):
    if n <= 0:
        return 0
    
    i = n
    denomirator = log(i*i+1)
    currect = numerator / denomirator

    return currect + S(n-1, x)

x = int(input("Введите х: "))
i = int(input("Введите i: "))
numerator = stepen(x,i)
print(S(x, i))#