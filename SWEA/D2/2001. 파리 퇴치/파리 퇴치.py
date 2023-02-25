T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(N)]
    sum_list = []

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            _sum = 0
            for k in range(M):
                _sum += sum(fly[i + k][j:j + M])
            sum_list.append(_sum)

    print(f'#{tc}', max(sum_list))
