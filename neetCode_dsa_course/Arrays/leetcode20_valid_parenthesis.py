def validParenthesis(s):
    myStack = []
    for i in s:
        if i in "({[":
            myStack.append(i)
        else:
            if (not myStack or \
                (i == "}" and myStack[-1] != "{") or \
                (i == "]" and myStack[-1] != "[") or \
                (i == ")" and myStack[-1] != "(")):
                return False
            else:
                myStack.pop()
    return not myStack

print(validParenthesis(")"))