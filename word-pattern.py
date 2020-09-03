def word_pattern(pattern, str):
    target = str.split(' ')
    if len(target) != len(pattern):
        return False
    p_collection = {}
    for i, v in enumerate(target):
        if v not in p_collection.values():
            if pattern[i] in p_collection.keys():
                if p_collection[pattern[i]] != v:
                    return False
            else:
                p_collection[pattern[i]] = v
        else:
            if list(p_collection.keys())[list(p_collection.values()).index(v)] != pattern[i]:
                return False
    return True


print(word_pattern('abba', 'dog dog cat dog'))


