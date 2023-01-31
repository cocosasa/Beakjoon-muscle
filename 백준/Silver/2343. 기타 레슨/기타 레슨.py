import sys
from collections import deque

N,M = map(int, input().split())
lesson = list(map(int,input().split()))

start =max(lesson)
end = sum(lesson)
ans=sys.maxsize
while start <= end: #적절한 블루레이크기를 찾는 알고리즘
    mid = (start+end) // 2
    cnt = 0
    tmp = 0 #블루레이크기값
    for i in lesson:
        if i + tmp > mid :
            tmp =0
            cnt +=1
        tmp += i
        
    if tmp :
        cnt +=1
    
    #범위 재설정

    if cnt > M:
        start = mid + 1
    else:
        ans=min(ans,mid)
        end = mid - 1     
print(ans)