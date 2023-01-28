M, N = map(int,input().split(' '))

B_start = []
W_start = []

for i in range(8) :
    row1 = ''
    row2 = ''
    for j in range(8) :
        if i % 2 :
            if j % 2 :
                row1 += 'B'
                row2 += 'W'
            else : 
                row1 += 'W'
                row2 += 'B'
        else :
            if j % 2 :
                row1 += 'W'
                row2 += 'B'
            else : 
                row1 += 'B'
                row2 += 'W'
    B_start.append(list(row1))
    W_start.append(list(row2))

chess_arr = []
min_cnt = 64

for i in range(M) :
    chess_arr.append(list(input().strip()))

for i in range(M-7) : 
    for j in range(N-7) :
        cnt1 = cnt2 = 0
        for k in range(8) :
            for m in range(8) :
                if chess_arr[k+i][m+j] != B_start[k][m] :
                    cnt1 += 1
                
                if chess_arr[k+i][m+j] != W_start[k][m] :
                    cnt2 += 1
        if min_cnt > min(cnt1,cnt2) :
            min_cnt = min(cnt1,cnt2)
            
print(min_cnt)
        
