def brute(k, cnt, line) :
    global min_line, max_connect
    if cnt + core_count - k < max_connect :
        return
    if k == core_count :
        if cnt > max_connect :
            max_connect = cnt
            min_line = line
        elif cnt == max_connect :
            if min_line > line :
                min_line = line
        return
    
    si, sj = cores[k]
    for di, dj in d :
        for l in range(1,N+1) :
            ni, nj = si + l*di, sj + l*dj
            if 0<=ni<N and 0<=nj<N :
                if arr[ni][nj] == 0:
                    continue
                else :
                    break
            else :
                for i in range(1,l) :
                    arr[si+i*di][sj+i*dj] = 2
                # print(*arr, sep='\n')
                # print()
                brute(k+1, cnt+1, line+l-1)
                for i in range(1,l) :
                    arr[si+i*di][sj+i*dj] = 0
                break
    brute(k+1, cnt, line)



T = int(input())

d = ((0,1),(1,0),(0,-1),(-1,0))

for tc in range(1, T+1) :
    N = int(input())

    arr = [list(map(int,input().split())) for _ in range(N)]
    max_connect = 0
    min_line = N**2

    cores = []
    # core_count = sum(sum(arr, []))
    core_count = 0
    for i in range(N) :
        for j in range(N) :

            if arr[i][j] :
                if not (i == 0 or i == N-1 or j == 0 or j == N-1 ):
                    cores.append((i,j))
                    core_count += 1
    
    brute(0,0,0)

    print(f'#{tc} {min_line}')