#2 1 вариант
s = "aeees" 
def count_vowels(s, i = 0, sum = 0):
	if i == len(s):
		return sum
	vowels = "aeoiu"
	if s[i] in vowels:
		return count_vowels(s, i+1, sum+1)
	else:
		return count_vowels(s, i+1, sum)
print(count_vowels(s))