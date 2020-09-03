def reverse_string(s):
    counter = 0
    while counter < len(s) / 2:
        temp = s[counter]
        s[counter] = s[len(s) - counter - 1]
        s[len(s) - counter - 1] = temp
        counter += 1
    return s


print(reverse_string(['h', 'e', 'l', 'l', 'o']))