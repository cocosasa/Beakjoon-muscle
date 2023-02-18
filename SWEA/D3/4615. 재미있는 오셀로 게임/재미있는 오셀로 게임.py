T = int(input().strip())
for tc in range(1,T+1) :
    N, M = map(int,input().split())

    log = [list(map(int,input().split())) for _ in range(M)]

    board = [[0]*(N+2) for i in range((N+2))]
    m = N//2 
    board[m][m] = board[m+1][m+1] = 2
    board[m][m+1] = board[m+1][m] = 1
    
    d = [(1,-1),(1,0),(1,1),(0,-1),(0,1),(-1,-1),(-1,0),(-1,1),]

    for i, j, color in log :
        board[i][j] = color
        for di,dj in d :
            candi = []
            for mul in range(1,N) :
                ni, nj = i + di*mul, j + dj*mul
                if board[ni][nj] == 0:
                    break
                elif board[ni][nj] != color :
                    candi.append((ni,nj))
                else :
                    while candi :
                        ii, jj = candi.pop()
                        board[ii][jj] = color
                    break
    b_count = 0
    w_count = 0
    for i in range(N+2) :
        b_count += board[i].count(1)
        w_count += board[i].count(2)
    print(f'#{tc} {b_count} {w_count}')