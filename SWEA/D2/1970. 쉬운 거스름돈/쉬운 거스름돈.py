T = int(input())

for tc in range(1,T+1):
    N = int(input())
    bills = (50000,10000,5000,1000,500,100,50,10)
    count = [0] * 8
    i = 0
    while i < 8 :
        count[i] += N // bills[i]
        N %= bills[i]
        i += 1
    print(f'#{tc}')
    print(*count)