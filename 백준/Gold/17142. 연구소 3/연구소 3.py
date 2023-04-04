from collections import deque
from itertools import combinations

N, M = map(int,input().split())

lab = [list(map(int,input().split())) for _ in range(N)]
ans = N**2
virus = []
blank = 0
for i in range(N) :
    for j in range(N) :
        if lab[i][j] == 2 :
            virus.append((i, j))
        elif lab[i][j] == 0 :
            blank += 1

comb_list = combinations(virus, M)
flag = False

for combi in comb_list :
    visited = [[0]*N for _ in range(N)]
    queue = deque(combi)
    for i , j in combi :
        visited[i][j] = 1
    time = 0
    blk = blank
    while queue and blk :
        time += 1
        for k in range(len(queue)) :
            i, j = queue.popleft()
            
            for di, dj in ((0,1),(1,0),(0,-1),(-1,0)) :
                ni, nj  = i + di, j + dj
                if 0<= ni < N and 0<= nj < N and lab[ni][nj] != 1 and visited[ni][nj] == 0 :
                    queue.append((ni,nj))
                    visited[ni][nj] = 1
                    if lab[ni][nj] == 0 :
                        blk -= 1
    if not blk :
        flag = True
        if time < ans :
            ans = time
    
if flag :
    print(ans)
else :
    print(-1)
