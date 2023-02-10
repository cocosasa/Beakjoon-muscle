T = int(input())

for tc in range(1, T + 1):
    t, p = input().split()

    N, M = len(t), len(p)

    cnt = 0
    i = 0
    while i < N - M + 1:
        flag = 1
        for j in range(M):
            if t[i + j] != p[j]:
                flag = 0
                break
        if flag:
            cnt += 1
            i += M
        else:
            i += 1
    print(f'#{tc} {N - M * cnt + cnt}')
