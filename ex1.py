#2 вариант
import math

def recursive_sum (n, x):
      if n == 1:
         return 1 + math.sqrt(abs(x))
return recursive_sum(n - 1, x) + (1 / n) + math.sqrt(abs(x))