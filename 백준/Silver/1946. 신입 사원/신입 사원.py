import sys

T = int(input())

for i in range(T) :
    N = int(input())
    cnt = 1
    Rank = sorted([list(map(int,sys.stdin.readline().strip().split())) for _ in range(N)])
    
    Max = Rank[0][1]

    for j in range(1,N) :
        if Max > Rank[j][1] :
            cnt +=1
            Max = Rank[j][1]
    print(cnt)
