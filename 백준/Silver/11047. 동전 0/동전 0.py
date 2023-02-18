N, K = map(int,input().split())

coins = [int(input()) for _ in range(N)]

i = N-1
ans = 0
while K != 0 :
    ans +=  K // coins[i]
    K %= coins[i]
    i -= 1
        
print(ans)