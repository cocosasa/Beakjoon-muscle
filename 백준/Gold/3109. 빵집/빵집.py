from collections import deque

def dfs(ci, cj) :
    if cj == c-1 :
        return True
    arr[ci][cj] = 'x'
    for di, dj in d :
        ni, nj = ci + di, cj + dj
        if arr[ni][nj] == '.' :
            if dfs(ni,nj) :
                return True
    return False

r, c = map(int,input().split())

arr = [list('x'*c)]+[list(input()) for _ in range(r)]+[list('x'*c)]

d = ((-1,1), (0,1), ( 1, 1))

# print(arr)

ans = 0
for i in range(1, r+1):
    is_possible = dfs(i, 0)
    if is_possible :
        ans += 1
            
print(ans)
