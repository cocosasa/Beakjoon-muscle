import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int,input().split())

arr = [list(map(int,input().rstrip().split())) for _ in range(N) ]

cnt = 0
time = 0

for i in range(N) :
    for j in range(M) :
        if arr[i][j] == 1 :
            cnt += 1

while cnt> 0 :
    visited = [[0]*M for i in range(N)]
    queue = deque()
    queue.append((0,0))
    while queue :
        ci, cj = queue.popleft()
        for di, dj in ((0,1),(1,0),(0,-1),(-1,0)) :
            ni,nj = ci + di, cj + dj
            if 0<=ni<N and 0<= nj < M : 
                if arr[ni][nj] != 1 and visited[ni][nj] == 0 :
                    queue.append((ni,nj))
                    visited[ni][nj] = 5
                elif arr[ni][nj] == 1 :
                    visited[ni][nj] += 1
    for i in range(N) :
        for j in range(M) :
            if 1 < visited[i][j] < 5 :
                arr[i][j] = 0
                cnt -= 1
    time +=1
print(time)