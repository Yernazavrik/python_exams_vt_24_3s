#Вариант 4
def rec(n):
	if n == 1:
		return ((-1)/(2+1))
	return ((-1**n)/((2*n + 1)*n)) + rec(n - 1)

print(rec(2))

