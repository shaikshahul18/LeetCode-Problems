def isValid(s):
    stack = []
    for char in s:
        if char in "([{":
            stack.append(char)
        else:
            if not stack or \
                (char == ")" and stack[-1] != "(") or \
                (char == "}" and stack[-1] != "{") or \
                    (char == "]" and stack[-1] != "["):
                return False
            stack.pop()
    return not stack


print(isValid("()"))
print(isValid("()[]{}"))
