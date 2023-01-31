N,M = map(int, input().split())
tree = list(map(int,input().split()))
start, end = 1, max(tree) #이분탐색 검색 범위 설정

while start <= end: #적절한 벌목 높이를 찾는 알고리즘
    mid = (start+end) // 2
    
    tmp = 0 #벌목된 나무 총합
    for i in tree:
        if i >= mid:
            tmp += i - mid
    
    #범위 재설정
    if tmp >= M:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)    