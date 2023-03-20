from collections import deque
N, M = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N) ]

cnt = 0
time = 2 # 2부터 시작하여 마지막에 2를 빼줌

for i in range(N) :
    for j in range(M) :
        if arr[i][j] == 1 :
            cnt += 1

while cnt> 0 :
    visited = [[0]*M for i in range(N)]
    melt = []
    queue = deque()
    queue.append((0,0))
    while queue :
        ci, cj = queue.popleft()

        for di, dj in ((0,1),(1,0),(0,-1),(-1,0)) :
            ni,nj = ci + di, cj + dj
            if 0<=ni<N and 0<= nj < M and arr[ni][nj] != 1 and visited[ni][nj] == 0 :
                queue.append((ni,nj))
                visited[ni][nj] = 1
                arr[ni][nj] = time
    for i in range(N) :
        for j in range(M) :
            if arr[i][j] == 1 :
                air = 0
                for di, dj in ((0,1),(1,0),(0,-1),(-1,0)) :
                    ni,nj = i + di, j + dj
                    if arr[ni][nj] == time :
                        air += 1
                if air >= 2 :
                    melt.append((i,j))
    for mi, mj in melt :
        arr[mi][mj] = time
        cnt -= 1
    time +=1
print(time - 2)