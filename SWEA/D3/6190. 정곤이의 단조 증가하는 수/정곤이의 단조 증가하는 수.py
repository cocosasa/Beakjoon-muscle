T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    ans = []
    _max = -1
    for i in range(N):
        for j in range(i+1,N):
            ans.append(arr[i] * arr[j])

    for num in ans:
        listnum = list(map(int,str(num)))
        for i in range(0,len(listnum)-1) :
            if listnum[i] > listnum[i+1] :
                break
        else :
            if _max < num :
                _max = num
    print(f'#{tc}', _max)
