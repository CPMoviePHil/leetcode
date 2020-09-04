def is_anagram(s, t):
    s_collection = {}
    t_collection = {}
    for v in s:
        if v not in s_collection.keys():
            s_collection[v] = 1
        else:
            s_collection[v] += 1
    for v in t:
        if v not in t_collection.keys():
            t_collection[v] = 1
        else:
            t_collection[v] += 1
    for i, v in t_collection.items():
        if i not in s_collection.keys():
            return False
        else:
            if s_collection[i] != v:
                return False
    return True

print(is_anagram('hello', 'ollhef'))