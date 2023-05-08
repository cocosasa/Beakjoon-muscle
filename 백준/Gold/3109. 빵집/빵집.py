r, c = map(int,input().split())

arr = [list('x'*c)]+[list(input()) for _ in range(r)]+[list('x'*c)]

d = ((1,1), (0,1), ( -1, 1))

ans = 0
for i in range(1, r+1):
    stack = []
    if arr[i][0] == 'x' :
        continue
    stack.append((i, 0))
    while stack :
        si, sj = stack.pop()
        arr[si][sj] = 'x'
        if sj == c-1 :
            ans += 1
            break
        for di, dj in d :
            ni, nj = si + di, sj + dj
            if arr[ni][nj] == '.' :
                stack.append((ni,nj))
print(ans)
