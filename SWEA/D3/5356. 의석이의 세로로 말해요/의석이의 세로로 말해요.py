T = int(input())

for tc in range(1,T+1) :

    strings = [input() for _ in range(5)]

    for i in range(5) :
        tmp_len = len(strings[i])
        if tmp_len < 15 :
            strings[i] += '@' * (15 - tmp_len)
    print(f'#{tc}', end=' ')
    for j in range(15) :
        for i in range(5) :
            if strings[i][j] != '@' :
                print(strings[i][j], end='')
    print()
