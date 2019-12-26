def palindrome(my_integer):
    if my_integer < 0:
        return False
    int_str = str(my_integer)
    int_len = len(int_str)
    int_len_divided = len(int_str) // 2
    counter = 0
    while counter < int_len_divided:
        if int_str[counter] != int_str[int_len - counter - 1]:
            return False
        counter += 1
    return True


print(palindrome(131))
