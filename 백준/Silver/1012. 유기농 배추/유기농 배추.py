from collections import deque

def bfs(y,x): 
    if Map[y][x] != 1 :
        return
    
    global land
    
    pueue = deque()
    
    pueue.append((y,x))
    Map[y][x] = land
    while pueue :
        yy , xx = pueue.popleft()
        for n in range(4) :
            ny, nx = yy + d[n][0],xx+d[n][1]
            
            if 0<=nx<M and 0<=ny<N :
                if Map[ny][nx] == 1 :
                    pueue.append((ny,nx))
                    Map[ny][nx] = land
    land += 1



T = int(input())

for tc in range(T) :
    N,M ,K = map(int,input().split())
    
    vechu = [list(map(int,input().split())) for _ in range(K)]
    Map = [[0]*M for _ in range(N)]
    for y,x in vechu :
        Map[y][x] = 1
    land = 2

    d = [[0,1],[1,0],[0,-1],[-1,0]]
    for i in range(N) :
        for j in range(M) :
            bfs(i,j)


    print(land - 2)