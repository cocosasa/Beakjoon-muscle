T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    pari = [list(map(int, input().split())) for _ in range(N)]

    d = [[(1, 0), (0, -1), (-1, 0), (0, 1)], [(1, -1), (-1, -1), (-1, 1), (1, 1)]]
    _max = 0
    for i in range(N):
        for j in range(N):
            for k in range(2):
                tmp = pari[i][j]
                for di, dj in d[k]:
                    for m in range(1, M):
                        ni, nj = i + di * m, j + dj * m
                        if 0 <= ni < N and 0 <= nj < N:
                            tmp += pari[ni][nj]
                if _max < tmp:
                    _max = tmp
    print(f'#{tc}', _max)
