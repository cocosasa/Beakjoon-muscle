N = int(input())

Ps= list(map(int,input().split()))

Ps.sort()
ans = 0

for i in range(1,N+1) :
    ans += Ps[-i]*(i)

print(ans)