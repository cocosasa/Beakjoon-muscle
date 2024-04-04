import heapq

n = int(input())

arr = []

for i in range(n) :
    nums = map(int, input().split())
    
    for num in nums :
        if len(arr) < n :  
                heapq.heappush(arr, num)
        else :  #힙의 길이를 n으로 유지
            if arr[0] < num: #가장 작은 수보다 크다면 업데이트
                heapq.heappop(arr)
                heapq.heappush(arr, num)
print(arr[0])