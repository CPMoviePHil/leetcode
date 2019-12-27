def roman_to_int(s):
    roman_list = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    roman_list_value = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    counter = {}
    i = 0
    len_str = len(s)
    while i < len_str:
        if s in roman_list:
            return roman_list_value['s']
        if s[i] in counter.keys():
            counter[s[i]] += 1
        else:
            counter[s[i]] = 1
        i += 1
    return counter


print(roman_to_int('LVIII'))
print(roman_to_int('IV'))
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# I, II, III, IV, V, VI, VII, VIII, XI, X

