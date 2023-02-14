T = int(input())

for tc in range(1,T+1) :

    N = int(input())

    price = list(map(int,input().split()))
    revenue = 0
    i = N-1
    j = i - 1
    while i != 0 :
        while price[j] <= price[i] :
            revenue += price[i] - price[j]
            j -= 1
            if j == -1 :
                break
        if j == -1 :
            break
        i = j
    print(f'#{tc} {revenue}')