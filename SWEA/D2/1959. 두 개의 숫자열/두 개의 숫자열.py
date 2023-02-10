T = int(input())

cnt = 0
for test_case in range(1, T + 1):

    A, B = map(int, input().split())
    arrA = list(map(int, input().split()))
    arrB = list(map(int, input().split()))

    cnt = cnt + 1
    max = 0
    K = abs(A - B) + 1

    for i in range(K):
        sum = 0
        for j in range(min(A, B)):
            if min(A, B) == A:
                sum = sum + arrA[j] * arrB[j + i]
            else:
                sum = sum + arrA[j + i] * arrB[j]
        if max < sum:
            max = sum
    print(f'#{cnt} {max}')
