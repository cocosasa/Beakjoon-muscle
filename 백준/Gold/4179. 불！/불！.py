from collections import deque
def bfs() :
    Q = []
    tmp = []
    len_J = 1
    len_F = 0
    J_visit = [[0]*C for _ in range(R)]
    for i in range(R) :
        for j in range(C) :
            if maze[i][j] == 'J' :
                Q.append((i,j))
                J_visit[i][j] = 1
            elif maze[i][j] == 'F' :
                tmp.append((i,j))
                len_F += 1
    Q += tmp
    Q = deque(Q)
    time = 0
    while len_J > 0 :
        time += 1
        for _ in range(len_J) :
            mi, mj = Q.popleft()
            len_J -= 1
            if maze[mi][mj] == 'F' :
                continue
            for di, dj in d :
                nmi, nmj = mi + di , mj + dj
                if 0<= nmi < R and 0<= nmj < C :
                    if maze[nmi][nmj] == '.' and J_visit[nmi][nmj] == 0:
                        Q.append((nmi,nmj))
                        J_visit[nmi][nmj] = 1
                        len_J += 1
                        maze[nmi][nmj] = 'J'
                else :
                    return time
            maze[mi][mj] = '.'

        for _ in range(len_F) :
            fi, fj = Q.popleft()
            len_F -= 1
            for di, dj in d :
                nfi, nfj = fi + di , fj + dj
                if 0<= nfi < R and 0<= nfj < C and maze[nfi][nfj] != '#' and maze[nfi][nfj] != 'F':
                    Q.append((nfi,nfj))
                    len_F += 1
                    maze[nfi][nfj] = 'F'
    return 'IMPOSSIBLE'


R, C = map(int,input().split())
maze = [list(input()) for _ in range(R)]
d = ((0,1),(1,0),(0,-1),(-1,0))
# J : 지훈    F : 불    . : 길     # : 벽
# 불이 한칸씩 퍼지고 사람은 도망가는데 도망갈 위치를 큐에 넣는다 while q가 중첩으로 사람이 나가는데 성공하면 리스트에 넣고 
# 리스트가 비어있으면 IMPOSSIBLE
print(bfs())
