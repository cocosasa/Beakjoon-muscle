def dfs(si, sj, last) :
    if si == N-1 and sj == M-1 :
        return 1
    if possible[si][sj] == -1 :
        return 0
    possible_cnt = 0
    for di, dj in d :
        ni, nj = si + di, sj + dj
        if 0<= ni < N and 0<= nj < M :
            if target <= road[ni][nj] < last :
                if possible[ni][nj] > 0 :
                    possible_cnt += possible[ni][nj]
                else :
                    possible_cnt += dfs(ni, nj, road[ni][nj])
    if possible_cnt > 0 :
        possible[si][sj] = possible_cnt
    else :
        possible[si][sj] = -1
    return possible_cnt
            
N, M = map(int,input().split())

road = [list(map(int,input().split())) for _ in range(N)]
possible = [[0]*M for _ in range(N)]
d = ((0,1),(1,0),(0,-1),(-1,0))
target = road[N-1][M-1]

print(dfs(0,0,road[0][0]))