from itertools import combinations

N = int(input())
board = [list(map(int,input().split())) for i in range(N)]
nums = list(range(0,N))

C = list()

for i in range(N+1):
    for x in combinations(nums,i):
        C.append(x)
        
answer = -(float("inf"))

s = list() # 모든 열의 합

for i in range(N):
    tmp = 0
    for j in range(N):
        tmp += board[j][i]
    s.append(tmp)

for row_comb in C:
    ans_tmp = 0 
    for i in range(N):
        tmp = 0

        for rows in row_comb: 
            tmp += board[rows][i]
        ans_tmp += min(s[i]-tmp , tmp)
    answer = max(ans_tmp,answer)
    
print(answer)