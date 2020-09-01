def str_index(haystack, needle):
    if needle == '':
        return 0
    for i, v in enumerate(haystack):
        if v == needle[0]:
            if haystack[i:i+len(needle)] == needle:
                return i
    return -1


print(str_index("mississippi", "issip"))
