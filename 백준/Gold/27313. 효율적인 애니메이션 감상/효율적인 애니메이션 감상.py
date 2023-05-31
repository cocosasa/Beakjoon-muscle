import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
times = list(map(int, input().split()))


times.sort()

dp = [0]*N
for i in range(N) :
    if i < K :
        time = times[i]
    else :
        time = dp[i-K] + times[i]
    if time > M :
        ans = i
        break
    dp[i] = time
else :
    ans = N
print(ans)