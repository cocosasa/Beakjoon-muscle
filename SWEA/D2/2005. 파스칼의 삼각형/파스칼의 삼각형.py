T = int(input())

for tc in range(1, T+ 1) :
    N = int(input())
    print(f'#{tc}')
    arr = [1]

    for i in range(1,N+1) :
        print(*arr)
        newarr = arr.copy()
        newarr.append(1)
        for j in range(1,i):
            newarr[j] += arr[j-1]
        arr = newarr