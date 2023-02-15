T = int(input())

for tc in range(1, T + 1):
    brak = input()
    brak = brak.replace('()', 'L')
    stack = []
    stick = 0
    for b in brak:
        if b == 'L':
            stick += len(stack)
        elif b == '(':
            stack.append(b)
        elif b == ')':
            stack.pop()
            stick += 1
    print(f'#{tc}', stick)
