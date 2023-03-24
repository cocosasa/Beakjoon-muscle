N, M = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]
move = []
for i in range(M) :
    move.append(list(map(int,input().split())))
    
d = ((0,0),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1))
clouds = [(N-1,0),(N-1,1),(N-2,0),(N-2,1)]
for i in range(M) :
    rained = []
    direc , s = move[i]
    # 비이동
    for j in range(len(clouds)) :
        ci, cj = clouds[j]
        ni, nj = ci + s * d[direc][0], cj + s * d[direc][1]
        ni %= N
        nj %= N
        arr[ni][nj] += 1
        rained.append((ni,nj))
    # 물복사
    for j in range(len(rained)) :
        cnt = 0 
        for di, dj in d[2::2] :
            ni, nj = rained[j][0] + di ,rained[j][1] + dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] > 0 :
                cnt += 1
        arr[rained[j][0]][rained[j][1]] += cnt
    
    #구름생성
    newclouds = []
    for j in range(N) :
        for k in range(N) :
            if (j,k) in rained :
                continue
            if arr[j][k] >= 2 :
                arr[j][k] -= 2
                newclouds.append((j,k))
    clouds = newclouds
ans = 0

for i in range(N) :
    ans += sum(arr[i])
    
print(ans)