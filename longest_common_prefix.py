def longest_common_prefix(strs):
    len_strs = len(strs)
    prefix = ''
    if not strs:
        return prefix
    least_len = {'length': len(my_list[0]), 'index':0}
    for index, value in enumerate(strs):
        if least_len['length'] > len(value):
            least_len['length'] = len(value)
            least_len['index'] = index
    for index, value in enumerate(strs[least_len['index']]):
        counter = 0
        times = 0
        while counter < len_strs:
            if value == strs[counter][index]:
                times += 1
            if times == len_strs:
                prefix += value
            counter += 1
        if index == 0 and prefix == '':
            return ''
    return prefix


my_list = ["flower","flow","flight"]
print(longest_common_prefix(my_list))