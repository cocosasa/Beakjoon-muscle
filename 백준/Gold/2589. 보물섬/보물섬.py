from collections import deque

def bfs(_map, ii, jj):
    # 여기가 L인지 W인지
    de = deque([(ii,jj,0)])
    visited[ii][jj] = True

    while de :
        ci, cj, distance = de.popleft()

        for i in range(4):
            ni = ci + di[i]
            nj = cj + dj[i]
            if 0 <= ni < N and 0 <= nj < M:
                if _map[ni][nj] == 'L' and visited[ni][nj] == False:
                    de.append((ni,nj,distance+1))
                    visited[ni][nj] = True
    return distance

N, M = map(int, input().split())

Map = [list(input()) for _ in range(N)]

di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]
dd = []
for i in range(N):
    for j in range(M):
        d = 0
        if Map[i][j] == 'L':
            visited = [[False] * M for i in range(N)]
            d = bfs(Map, i, j)
        if d :
            dd.append(d)

ans = max(dd)

print(ans)
