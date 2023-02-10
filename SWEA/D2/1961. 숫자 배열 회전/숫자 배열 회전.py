T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = []
    for i in range(1, N + 1):
        arr.append(list(map(int, input().split(" "))))
    print(f'#{test_case}')
    for i in range(N):
        for j in range(N):
            print(arr[-j - 1][i], end="")
        print(" ", end="")
        for j in range(N):
            print(arr[-i - 1][-j - 1], end="")
        print(" ", end="")
        for j in range(N):
            print(arr[j][-i - 1], end="")
        print("")