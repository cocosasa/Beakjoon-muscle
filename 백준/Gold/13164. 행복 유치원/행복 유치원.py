n, k = map(int,input().split())
ki = list(map(int,input().split()))
M = []
for i in range(n-1) :
    M.append(0)
    M[i] = ki[i+1] - ki[i]
M.sort()
del M[n-k:]
cost = sum(M)
print(cost)
