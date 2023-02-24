s = list(input())
c4 = list(input())
stack = []
length = 0
c4len = len(c4)
for c in s :
    stack.append(c)
    length += 1
    if length >= c4len and stack[-c4len:] == c4:
        for i in range(c4len) :
            stack.pop()
            length -= 1
if length :
    print(''.join(stack))
else :
    print('FRULA')

