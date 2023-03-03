d = ((0, 1), (1, 0), (-1, 0), (0, -1))

N = int(input())
PAPER = 103

arr = [[0] * PAPER for _ in range(PAPER)]

for _ in range(N):
    y, x = map(int, input().split())
    for i in range(y + 1, y + 11):
        for j in range(x + 1, x + 11):
            arr[i][j] = 5

ans = 0

for i in range(PAPER):
    for j in range(PAPER):
        if arr[i][j] == 5:
            for di, dj in d:
                ni, nj = i + di, j + dj
                if ni > 102 or nj > 102 or ni < 0 or nj < 0:
                    continue
                if arr[ni][nj] == 5:
                    continue
                ans += 1
print(ans)