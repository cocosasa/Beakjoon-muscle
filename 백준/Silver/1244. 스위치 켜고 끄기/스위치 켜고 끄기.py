N = int(input())
switch = [3] + list(map(int,input().split()))
M = int(input())
students = [list(map(int,input().split())) for _ in range(M)]

for boygirl, num in students :

    if boygirl == 2: # 여자
        switch[num] = (switch[num] + 1 ) % 2
        for i in range(1,N+1) :
            nleft = num - i
            nright  = num + i
            if 0 <= nleft< N+1 and 0 <= nright < N+1 :
                if switch[nleft] == switch[nright] :
                    switch[nleft] = (switch[nleft] + 1 ) % 2
                    switch[nright] = (switch[nright] + 1) % 2
                else :
                    break
            else :
                break
    else :
        for i in range(num,N+1,num) :
            switch[i] = (switch[i]+1 ) % 2

for i in range(1 ,N+1) :
    print(switch[i],end=' ')
    if i % 20 == 0 :
        print()


