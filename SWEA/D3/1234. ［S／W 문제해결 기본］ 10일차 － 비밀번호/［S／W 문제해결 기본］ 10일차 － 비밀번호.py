for tc in range(1,11) :
    N , s = input().split()
    stack = []
    for i in range(int(N)) :
        if stack :
            if stack[-1] != s[i] :
                stack.append(s[i])
            else :
                n = stack.pop()
        else :
            stack.append(s[i])
    print(f'#{tc} {"".join(stack)}')