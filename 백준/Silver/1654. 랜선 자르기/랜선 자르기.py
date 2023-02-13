K, N = map(int, input().split())

lan = list(int(input()) for _ in range(K))

total = sum(lan)
start = 1
end = max(lan)

while start <= end :
    mid = (start + end) // 2
    new = 0
    for l in lan:
        new += l // mid
    if new >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)
