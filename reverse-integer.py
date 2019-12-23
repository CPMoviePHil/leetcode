def reverse(my_integer):
    is_negative = False
    temp_dict = {}
    reversed_number = ''
    str_int = str(my_integer)
    for index, value in enumerate(str_int):
        if index == 0 and value == '-':
            is_negative = True
        elif index == 0:
            temp_dict[0] = str_int[len(str_int)-1]
        else:
            if is_negative:
                temp_dict[index] = str_int[len(str_int) - index]
            else:
                temp_dict[index] = str_int[len(str_int) - index - 1]
    if is_negative:
        reversed_number = '-'
    for number in temp_dict.values():
        reversed_number += str(number)
    if is_negative:
        if int(reversed_number) < -2**31:
            return 0
        else:
            return int(reversed_number)
    else:
        if int(reversed_number) > 2**31-1:
            return 0
        else:
            return int(reversed_number)


print(reverse(-123))

