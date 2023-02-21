def bfs(si, sj, time):
    Q = [(si, sj)]
    visited[si][sj] = 1
    for t in range(time - 1):
        for i in range(len(Q)):
            i, j = Q.pop(0)
            pipe = Map[i][j]
            for di, dj in d[pipe]:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] != 1 and (i, j) in adjL[ni][nj]:
                    Q.append((ni, nj))
                    visited[ni][nj] = 1


T = int(input())

d = (
    ((0, 0)), ((-1, 0), (0, 1), (0, -1), (1, 0)), ((-1, 0), (1, 0)), ((0, -1), (0, 1)), ((-1, 0), (0, 1)),
    ((1, 0), (0, 1)),
    ((1, 0), (0, -1)), ((0, -1), (-1, 0)))

for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())

    Map = [list(map(int, input().split())) for _ in range(N)]
    adjL = [list([] for i in range(M)) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            pipe = Map[i][j]
            if pipe != 0:
                for di, dj in d[pipe]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < M:
                        adjL[i][j].append((ni, nj))
    visited = [[0] * M for _ in range(N)]
    ans = 0
    bfs(R, C, L)
    for i in range(N):
        ans += sum(visited[i])
    print(f'#{tc}', ans)
