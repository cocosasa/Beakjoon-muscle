def check() :
    _max = 0
    for i in range(N):
        c1 = board[i][0]
        c2 = board[0][i]
        cnt_r = 0
        cnt_c = 0
        for j in range(N) :
            if board[i][j] == c1 :
                cnt_r += 1
                if _max < cnt_r :
                    _max = cnt_r
            else :
                c1 = board[i][j]
                cnt_r = 1
            if board[j][i] == c2 :
                cnt_c += 1
                if _max < cnt_c :
                    _max = cnt_c
            else :
                c2 = board[j][i]
                cnt_c = 1
    if _max < cnt_c :
        _max = cnt_c
                
    if _max < cnt_r :
        _max = cnt_r
    return _max
            

N = int(input())

board = [list(input()) for _ in  range(N)]
ans = [1]

for i in range(N) :
    for j in range(N-1) :
        if board[i][j] != board[i][j+1] :
            board[i][j] ,board[i][j+1] = board[i][j+1] ,board[i][j]
            ans.append(check())
            board[i][j] ,board[i][j+1] = board[i][j+1] ,board[i][j]
for j in range(N) :
    for i in range(N-1) :
        if board[i][j] != board[i+1][j] :
            board[i][j] ,board[i+1][j] = board[i+1][j] ,board[i][j]
            ans.append(check())
            board[i][j] ,board[i+1][j] = board[i+1][j] ,board[i][j]

print(max(ans))