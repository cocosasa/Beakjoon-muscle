from collections import deque
import sys; input = sys.stdin.readline

def bfs(si, sj) :
    queue = deque()
    queue.append((si,sj))
    visited[si][sj] = land
    
    while queue :
        i, j = queue.popleft()

        for di, dj in d :
            ni, nj = i + di , j + dj 
            if 0<= ni < row and 0<= nj < col and arr[ni][nj] and not visited[ni][nj] :
                queue.append((ni,nj))
                visited[ni][nj] = land

row, col = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(row)]
d = ((0,1),(1,0),(0,-1),(-1,0))

ans = 1
ice = 0
for i in range(row) :
    for j in range(col) :
        if arr[i][j] :
            ice += 1

while ice :
    melt = [[0]* col for _ in range(row)]
    for i in range(row) :
        for j in range(col) :
            if arr[i][j] :
                cnt = 0
                for di, dj in d :
                    ni, nj = i + di, j + dj
                    if 0<= ni < row and 0<= nj < col and not arr[ni][nj] :
                        cnt += 1
                melt[i][j] = cnt
    new_zero = False
    for i in range(row) :
        for j in range(col) :
            if melt[i][j] :
                next = arr[i][j] - melt[i][j]
                if next <= 0 :
                    arr[i][j] = 0
                    new_zero = True
                    ice -= 1
                else :
                    arr[i][j] = next
    
    land = 0
    if new_zero :
        visited = [[0]*col for _ in range(row)]
        for i in range(row) :
            for j in range(col) :
                if arr[i][j] and not visited[i][j]:
                    land += 1
                    bfs(i,j)
                    
    if land >= 2 :
        break
    ans += 1
if ice :
    print(ans)
else :
    print(0)
