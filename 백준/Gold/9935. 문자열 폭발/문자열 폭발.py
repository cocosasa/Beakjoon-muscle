s = list(input())
c4 = list(input())
stack = []
length = 0
c4len = len(c4)
for i in range(len(s)) :
    stack.append(s[i])
    length += 1
    if length >= c4len and stack[-c4len:] == c4:
        for i in range(c4len) :
            stack.pop()
            length -= 1
if len(stack) :
    print(''.join(stack))
else :
    print('FRULA')

