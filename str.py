def concatenate(n):
    n = abs(n)          # на всякий случай, если число отрицательное
    if n < 10:
        return str(n)
    return concatenate(n // 10) + str(n % 10)

# ввод:
x = int(input("Введите число: "))
print(concatenate(x))
