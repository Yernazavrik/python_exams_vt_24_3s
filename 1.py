def perfectnumber(s):
    digits = "0123456789_"
    list1 = []
    list_final = []

    def remove_word(s_f, i = 0):
        if i == len(s):
            return ""
        if s[i] in digits:
            return s[i] + remove_word(s, i + 1)
        else:
            return remove_word(s, i + 1)

    def remove_(digit_slash, index, list, temp):
        digit_w = "0123456789"

        if index == len(digit_slash):
            return ""
        if digit_slash[index] in digit_w:
            temp += digit_slash[index]
            return  remove_(digit_slash, index+1, list, temp)
        if temp == "_" or temp == '':
            return remove_(digit_slash, index + 1, list, temp)
        else:
            return list.append(temp), remove_(digit_slash, index + 1, list, temp = '')
        
    def znak(znak_list, index, sum):
        if index >= int(znak_list):
            return 1
        if int(znak_list) % index == 0:
            sum = sum + index
            print(sum)
            return sum, znak(znak_list, index + 1, sum)
        else:
            return sum, znak(znak_list, index + 1, sum)


    def final_round(list2, index, list_final):
        if index == len(list2):
            return ""
        char = znak(list2[index], 1, 0)
        char_2 = char[0]
        print("___", char_2)
        if list2[index] == char_2:
            print("ABC")
            list_final.append(list2[index])
            return final_round(list2, index + 1, list_final), list_final
        
        else:
            final_round(list2, index + 1, list_final), list_final


    remove_(remove_word(s), 0, list1, '')
    return list_final, final_round(list1, 0, list_final)


	
s = input()
result = perfectnumber(s)
print(result[0])
	