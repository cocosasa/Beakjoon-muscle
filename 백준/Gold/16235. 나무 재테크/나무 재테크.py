import sys ; input = sys.stdin.readline

n ,m, K = map(int,input().split())

s2d2 = []
for r in range(n) :
    s2d2.append(list(map(int,input().split())))
    
yang = [[[] for _ in range(n)] for _ in range(n)]
bun = [[5]*n for _ in range(n)]
die = [[[] for _ in range(n)] for _ in range(n)]

for i in range(m) :
    x, y, z = map(int,input().split())
    yang[x-1][y-1].append(z)


dd = ((-1, -1), (0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1))

# print(*yang, sep='\n')

for k in range(K) :
    # 봄
    for i in range(n) :
        for j in range(n) :
            yang[i][j].sort()
            for h in range(len(yang[i][j])) :
                if bun[i][j] >= yang[i][j][h] :
                    bun[i][j] -= yang[i][j][h]
                    yang[i][j][h] += 1
                else :
                    die[i][j] = yang[i][j][h:]
                    yang[i][j] = yang[i][j][:h]
                    break
    # 여름
    for i in range(n) :
        for j in range(n) :
            for d in die[i][j] :
                if d//2 :
                    bun[i][j] += d//2
            die[i][j] = []
    # 가을
    for i in range(n) :
        for j in range(n) :
            cnt = 0
            for k in yang[i][j] :
                if k%5 == 0:
                    cnt += 1

            for di, dj in dd:
                ni, nj = i + di, j + dj
                if 0<= ni < n and 0<= nj < n :
                    yang[ni][nj] = [1]*cnt + yang[ni][nj]
    # 겨울 
    for i in range(n) :
        for j in range(n) :
            bun[i][j] += s2d2[i][j]

    # print(*yang, sep='\n')

total = 0
for i in range(n) :
    for j in range(n) :
        total += len(yang[i][j])
print(total)