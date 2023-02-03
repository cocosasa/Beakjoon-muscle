N = int(input())

Ps= list(map(int,input().split()))
arr = []
Ps.sort()
ans = 0
for i in range(1,N+1) :
    for j in range(i) :
        ans += Ps[j]
        
print(ans)