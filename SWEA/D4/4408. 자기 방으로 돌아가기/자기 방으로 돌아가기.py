T = int(input())

for tc in range(1,T+1) :
    N = int(input())
    backrooms = [list(map(int,input().split())) for _ in range(N)]
    count = [0] * 200

    for start , end in backrooms :
        if start > end :
            start, end = end, start
        for i in range((start-1)//2,(end-1)//2+1) :
            count[i] += 1

    print(f'#{tc}',max(count))