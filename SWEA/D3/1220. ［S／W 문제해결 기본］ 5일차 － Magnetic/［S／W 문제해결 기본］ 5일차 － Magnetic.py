T= 10
for tc in range(1,T+1) :
    N = int(input())
    table = [list(input().split()) for _ in range(N)]
    cnt = 0
    table = list(zip(*table))
    table = list(map(''.join,table))

    newtable = []
    for i in range(N) :
        tmp = ''
        for j in range(N) :
            if table[i][j] != '0' :
                tmp += table[i][j]
        newtable.append(tmp)
    for i in range(N) :
        cnt += newtable[i].count('12')

    print(f'#{tc}', cnt)