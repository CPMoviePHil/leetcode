def reverse(my_integer):
    counter = 0
    temp_dict = []
    quotient = my_integer
    is_negative = True if my_integer < 0 else False
    reversed_number = '-' if is_negative else ''
    if is_negative:
        quotient = quotient * -1
    while quotient > 9:
        reminder = quotient % 10
        temp_dict.append(reminder)
        quotient = (quotient - reminder) // 10
        counter += 1
    temp_dict.append(quotient)
    for value in temp_dict:
        reversed_number += str(value)
    return int(reversed_number)


print(reverse(12345))
print(reverse(-123456))
