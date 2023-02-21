def bfs(si,sj) :

    Q = [(si,sj)]
    miro[si][sj] = 9
    while Q :
        i, j = Q.pop(0)

        for di, dj in d :
            ni, nj = i + di, j+dj
            if 0<=ni<N and 0<= nj < N :
                if miro[ni][nj] == 3 :
                    return 1
                if miro[ni][nj] == 0 :
                    Q.append((ni,nj))
                    miro[ni][nj] = 9
    return 0


T = 10
d = ((0,1),(1,0),(0,-1),(-1,0))
for tc in range(1,T+1) :
    N = 16
    TC = input()
    miro = [list(map(int,input())) for _ in range(N)]

    for i in range(N):
        for j in range(N) :
            if miro[i][j] == 2 :
                ans = bfs(i,j)

    print(f'#{tc}',ans)