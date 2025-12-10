def concatenate_digits(n):
    table = {}

    def collect(x):
        if x == 0:
            return
        digit = x % 10
        table[digit] = True
        collect(x//10)

    collect(n)

    def build_string(d):
        if d > 9:
            return ""
        if table.get:
            return str(d) + build_string(d + 1)
        else:
            return build_string(d + 1)
        
    return build_string(0)

number = input("Введите число ")
print(concatenate_digits(number))