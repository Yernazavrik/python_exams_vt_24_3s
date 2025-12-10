def sum_of_unique_digit_squares(n):
    def helper(n, seen_digits):
        if n == 0:
            return 0

        digit = n % 10
        rest_sum = helper(n // 10, seen_digits)

        if digit in seen_digits:
            return rest_sum
        else:
            seen_digits.append(digit)
            return digit * digit + rest_sum
    
    return helper(n, seen_digits)

seen_digits = []
a = int(input("Введите число: "))
print(sum_of_unique_digit_squares(a))