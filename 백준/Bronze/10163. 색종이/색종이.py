import sys
input = sys.stdin.readline

N = int(input())

paper = [list(map(int,input().rstrip().split())) for _ in range(N)]

grid = [[0]*1001 for _ in range(1001)]
color = 1
ans = [0] * N
for sj, si, width, height in paper :

    for i in range(si, si+ height) :
        for j in range(sj , sj + width) :
            if j == 1001 :
                break
            grid[i][j] = color
        if i == 1000 :
            break
    color += 1

for i in range(1001) :
    for j in range(1001) :
        if grid[i][j] :
            ans[grid[i][j]-1] += 1
print(*ans,sep='\n')