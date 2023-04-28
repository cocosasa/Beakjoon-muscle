n = int(input())

info = [list(map(int, input().split())) for _ in range(n)]

_dir = [(0, 1), (-1, 0), (0, -1), (1, 0)]
N = 101
arr = [[0]*N for _ in range(N)]
ans = 0
for x, y, d, g in info:
    curve = [d]

    for year in range(g):
        curve += [(i+1)%4 for i in curve[::-1]]

    arr[x][y] = 1
    for d in curve:
        dy, dx = _dir[d]
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N:
            arr[nx][ny] = 1
        x, y = nx, ny

for i in range(N-1) :
    for j in range(N-1) :
        if arr[i][j] and arr[i][j+1] and arr[i+1][j] and arr[i+1][j+1] :
            ans += 1

print(ans)
