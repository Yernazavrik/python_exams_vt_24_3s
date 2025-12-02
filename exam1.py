#1 1 вариант
def rec(x, n, i=1, fact = 1, sum = 0, dec_fact = 3, dec_x = 2):
	if i> n:
		return (sum)
	dec_x += x*x
	dec_fact += fact*i
	print(dec_x)
	print(dec_fact)
	sum += x/dec_fact
	print(sum)
	print("***********")
	return rec(x, n, i+1, fact, sum, dec_fact, dec_x)
print(rec(2, 3)) # test
	