def longest_substring(s):
    count_len = []
    temp_s = []
    counter = 0
    if len(s) != 1:
        for v in s:
            if v not in temp_s:
                temp_s.append(v)
                if counter == len(s) - 1:
                    count_len.append(len(temp_s))
                    temp_s = []
            else:
                count_len.append(len(temp_s))
                if v != temp_s[-1]:
                    temp_s.remove(v)
                else:
                    temp_s = []
                temp_s.append(v)
            counter += 1
    else:
        count_len.append(1)
    return max(count_len) if len(count_len) != 0 else 0

print(longest_substring("ckilbkd"))