def bfs(si, sj):
    global area
    queue = [(si, sj)]
    color = grid[si][sj]
    while queue:
        i, j = queue.pop(0)
        for di, dj in dd:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and  color == grid[ni][nj] and visited[ni][nj] == 0:
                queue.append((ni, nj))
                visited[ni][nj] = 1
    area += 1


dd = ((0, 1), (1, 0), (-1, 0), (0, -1))

N = int(input())

grid = [(input()) for _ in range(N)]
ans = [0, 0]
area = 0
visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)

for i in range(N):
    grid[i] = grid[i].replace('G', 'R')

ans[0] = area
area = 0
visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
ans[1] = area

print(*ans)
