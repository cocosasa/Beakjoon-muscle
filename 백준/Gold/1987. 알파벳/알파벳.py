def dfs(si,sj,k) :
    global max_cnt
    if k > max_cnt: 
        max_cnt = k

    for di, dj in ((0,1),(1,0),(0,-1),(-1,0)) :
        ni, nj = si + di, sj + dj
        if 0<= ni < N and 0<= nj < M :
            alpha_idx = ord(arr[ni][nj])-65
            if  alpha_visited[alpha_idx] == 0 :
                alpha_visited[alpha_idx] = 1
                dfs(ni,nj,k+1)
                alpha_visited[alpha_idx] = 0

N, M = map(int,input().split())

arr = [list(input()) for _ in range(N)]
alpha_visited = [0]*26
alpha_visited[ord(arr[0][0])-65] = 1
max_cnt = 1
dfs(0,0,1)

print(max_cnt)