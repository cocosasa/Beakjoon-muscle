T= int(input())

for tc in range(1,T+1) :
    N, M, K = map(int,input().split())

    N_arr = list(map(int,input().split()))

    N_arr.sort(reverse=True)
    t = 0
    boong = -1* K
    flag = True
    while N_arr :
        if t % M == 0:
            boong += K
        if flag == False :
            break
        while t in N_arr :
            if N_arr[-1] != t :
                flag = False
                break
            if boong > 0 :
                N_arr.pop()
                boong -= 1
            else :
                flag = False
                break
        t += 1
    print(f'#{tc}',end=' ')
    if flag :
        print('Possible')
    else :
        print('Impossible')