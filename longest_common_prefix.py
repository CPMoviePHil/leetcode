def longest_common_prefix(my_list):
    len_strs = len(my_list)
    least_len = {'length': len(my_list[0]), 'index':0}
    prefix = ''
    counter = 0
    for index, value in enumerate(my_list):
        if least_len['length'] > len(value):
            least_len['length'] = len(value)
            least_len['index'] = index
    while counter < len_strs:
        for index, value in enumerate(my_list[least_len['index']]):
            if value == my_list[counter][index]:
                






my_list = ["flower","flow","flight"]
print(longest_common_prefix(my_list))