import sys
input = sys.stdin.readline

N, M = map(int,input().split())

arr = [list(input().rstrip()) for _ in range(N)]
history = [['']*M for _ in range(N)]
stack = []
stack.append((0,0,1,arr[0][0]))
max_cnt = 0
while stack :
    ci, cj, depth, route = stack.pop()
    max_cnt = max(max_cnt,depth)
    for di, dj in ((0,1),(1,0),(0,-1),(-1,0)) :
        ni, nj = ci + di, cj + dj
        if 0<= ni < N and 0<= nj < M and arr[ni][nj] not in route :
            new = route + arr[ni][nj]
            if new != history[ni][nj] :
                history[ni][nj] = new
                stack.append((ni,nj,depth+1,route + arr[ni][nj]))
print(max_cnt)