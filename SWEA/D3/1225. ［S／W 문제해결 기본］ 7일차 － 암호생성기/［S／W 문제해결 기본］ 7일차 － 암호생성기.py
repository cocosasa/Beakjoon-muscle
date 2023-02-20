for tc in range(1,11) :
    T = input()
    Q = list(map(int,input().split()))
    i = 1
    while True :
        tmp = Q.pop(0) - i
        i %= 5
        i += 1

        if tmp <= 0 :
            Q.append(0)
            break
        else :
            Q.append(tmp)

    print(f'#{tc}',*Q)