## Variant 4
## Task 1
def mul(a, b):
	if b == 0:
		return 0
	return a + mul(a, b-1)

def power(a,n):
	if n == 0:
		return 0
	return mul(a, power(a, n-1))
def s(x,i,n):
	if n > 0:
		return
	i2 = mul(i,i)
	i3 = mul(i2, i)
	s1 = i3 * i
	num = power(x, i2)
	return num / s1 (x, i + 1,n)
	print(s(2,1,5)) 

## Task 2
def flatten_dict(d, parent = "", res = None):
	if res is None:
		res = {}
	for key, value in d.items():
		new_key = key if parent == ""
	else parent + "_" + key
	if isinstance (value, dict):
		flatten_dict(value, new_key, result)
	else: 
		res[new_key] = value
	return(res)

print(flatten_dict({"a":{"b":1, "c":2}, "d": 3})
	
		
	
	