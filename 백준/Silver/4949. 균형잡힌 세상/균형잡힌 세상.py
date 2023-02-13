def checkBalance(s):
    for c in s:
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')' or c == ']':
            if not stack:
                return 'no'
            elif c == ')' and stack[-1] != '(' or c == ']' and stack[-1] != '[':
                return 'no'
            stack.pop()
    if stack:
        return 'no'
    return 'yes'

while True:
    s = input()
    if s == '.':
        break
    stack = []
    print(checkBalance(s))
