import sys
input = sys.stdin.readline

N, C = map(int,input().rstrip().split())

house = [int(input()) for _ in range(N)]

house.sort()
mindis = 1
maxdis = house[-1] - house[0]

while mindis <= maxdis  :
    cnt = 1
    mid = (mindis + maxdis)//2
    last = 0
    
    for i in range(1,N) :
        if mid <= house[i] - house[last] :
            last = i
            cnt += 1
    if cnt >= C :
        mindis = mid + 1
    else :
        maxdis = mid -1
print(maxdis)

