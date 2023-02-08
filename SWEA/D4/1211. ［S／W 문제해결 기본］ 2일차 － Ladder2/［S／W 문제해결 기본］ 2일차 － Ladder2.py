T = 10
 
for tc in range(1, T + 1):
    lee = input()
    ladder = [list(map(int, input().split())) for _ in range(100)]
    di = [0, 1, 0]
    dj = [-1, 0, 1]
    cnts = []
    for start in range(100) :
        cnt = 0
        if ladder[0][start] == 0 :
            cnts.append(10000)
            continue
        i = 0
        j = start
        state = 1
        while True:
            ni = i + di[state]
            nj = j + dj[state]
 
            if state == 1:
                if ni == 99 :
                    cnts.append(cnt)
                    break
                i = ni
                j = nj
                cnt += 1
                if nj == 0 and ladder[ni][nj + 1] == 1:
                    state = 2
                elif nj == 99 and ladder[ni][nj - 1] == 1:
                    state = 0
                elif nj != 0 and ladder[ni][nj - 1] == 1:
                    state = 0
                elif nj != 99 and ladder[ni][nj + 1] == 1:
                    state = 2
 
            else:
                if 0 <= nj < 100 and ladder[ni][nj] != 0:
                    i = ni
                    j = nj
                    cnt += 1
                else:
                    state = 1
    print(f'#{tc} {cnts.index(min(cnts))}')