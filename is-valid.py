def isValid(s):
    len_str = len(s)
    if s == '':
        return True
    if 0 <= len_str <= 1 or len_str % 2 == 1:
        return False
    stack = []
    for value in s:
        if value == '{':
            stack.append('{')
        elif value == '(':
            stack.append('(')
        elif value == '[':
            stack.append('[')
        if stack:
            if value == ']':
                if stack[-1] == '[':
                    stack.pop()
            if value == '}':
                if stack[-1] == '{':
                    stack.pop()
            if value == ')':
                if stack[-1] == '(':
                    stack.pop()
    if not stack:
        return True
    else:
        return False


print(isValid("[(])"))
