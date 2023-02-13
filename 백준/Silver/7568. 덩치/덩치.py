N = int(input())

data = list(tuple(map(int,input().split())) for _ in range(N))
rank = [1] * N

for i in range(N) :
    for kg, tall in data :
        if data[i][0] < kg and data[i][1] < tall :
            rank[i] += 1
print(*rank)