def f(n, m):
    if m == 1:
        return N
    return N * f(n, m - 1)


for tc in range(1, 10 + 1):
    t = input()

    N, M = map(int, input().split())

    print(f'#{tc}', f(N, M))
