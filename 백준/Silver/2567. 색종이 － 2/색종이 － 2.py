from collections import deque

def bfs(si, sj) :
    global ans
    Q = deque()
    Q.append((si,sj))
    arr[si][sj] = VISITED

    while Q :
        ii, jj = Q.popleft()

        for di, dj in d :
            ni, nj = ii + di, jj + dj
            if ni < 0 or ni > PAPER-1 or nj < 0 or nj > PAPER-1 :
                continue
            if arr[ni][nj] < BLACK :
                ans += 1
            elif arr[ni][nj] == BLACK :
                Q.append((ni,nj))
                arr[ni][nj] = VISITED

d = ((0,1),(1,0),(-1,0),(0,-1))

N = int(input())
PAPER = 103
BLACK = 6
VISITED = 7

arr = [[0]*PAPER for _ in range(PAPER)]

for _ in range(N) :
    y, x = map(int,input().split())
    for i in range(y+1,y+11) :
        for j in range(x+1,x+11) :
            arr[i][j] = BLACK

ans = 0

for i in range(PAPER) :
    for j in range(PAPER) :
        if arr[i][j] == BLACK :
            bfs(i,j)

print(ans)