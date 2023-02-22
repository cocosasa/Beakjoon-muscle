T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    ans = []
    _max = -1
    for i in range(N):
        for j in range(i + 1, N):
            num = arr[i] * arr[j]
            listnum = str(num)
            for k in range(len(listnum) - 1):
                if listnum[k] > listnum[k + 1]:
                    break
            else:
                if _max < num:
                    _max = num
    print(f'#{tc}', _max)
