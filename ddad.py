def perfectnumber(s):
    digits = "0123456789_"
    
    def remove_word(s, i=0):
        if i == len(s):
            return ""
        if s[i] in digits:
            return s[i] + remove_word(s, i + 1)
        else:
            return remove_word(s, i + 1)
    
    def remove_(digit_slash, index, list, temp):
        digit_w = "0123456789"
        
        if index == len(digit_slash):
            if temp not in ("_", "") and temp != '':
                list.append(temp)
            return
        
        if digit_slash[index] in digit_w:
            temp += digit_slash[index]
            remove_(digit_slash, index+1, list, temp)
        else:
            if temp not in ("_", "") and temp != '':
                list.append(temp)
            remove_(digit_slash, index + 1, list, temp='')
    
    def is_perfect(num_str):
        try:
            n = int(num_str)
            if n <= 0:
                return False
            sum_divisors = 0
            for i in range(1, n//2 + 1):
                if n % i == 0:
                    sum_divisors += i
            return sum_divisors == n
        except ValueError:
            return False
    
    def final_round(list2, index, list_final):
        if index == len(list2):
            return list_final
        
        if is_perfect(list2[index]):
            list_final.append(list2[index])
        
        return final_round(list2, index + 1, list_final)
    
    list1 = []
    list_final = []
    
    remove_(remove_word(s), 0, list1, '')
    final_round(list1, 0, list_final)
    
    return list_final


s = input()
result = perfectnumber(s)
print(result)