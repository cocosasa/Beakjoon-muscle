N = int(input())
index = list(map(int,input().split()))
ans = [1]
for i in range(1,N) :
    ans.insert(i-index[i],i+1)
print(*ans)
