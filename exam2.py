#2 1 вариант
s = "abcde" 
def count_vowels(s, i = 0, sum = 0):
	if s == "":
		return sum
	vowels = "aeoiu"
	print(s[i])
	if s[i] in vowels:
		s[i] =""
		return count_vowels(s, i+1, sum+1)
print(count_vowels(s))