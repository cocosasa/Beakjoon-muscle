T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    farm = [list(map(int, input())) for _ in range(N)]
    K = N // 2
    val = 0
    for i in range(N):
        for j in range(abs(K - i), N - abs(K - i)):
            val += farm[i][j]
    print(f'#{tc}', val)
