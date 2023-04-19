def dfs(k, tmpset) :
    global min_blank
    if k == CCTV_COUNT :
        # print(tmpset)
        blank = total_blank - len(tmpset)
        if min_blank > blank :
            min_blank = blank
        return
    for cover in cctv_cover[k] :
        dfs(k+1, tmpset|cover )

n, m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

d = ((0,1),(1,0),(0,-1),(-1,0))


CCTV = {
    1:((0,),(1,),(2,),(3,)),
    2:((0,2),(1,3)),
    3:((0,1),(1,2),(2,3),(3,0)),
    4:((0,1,2),(0,1,3),(0,2,3),(1,2,3),),
    5:((0,1,2,3),),
}

cctvs = []
total_blank = 0
for i in range(n) :
    for j in range(m) :
        if arr[i][j] == 0 :
            total_blank += 1
        elif 1<= arr[i][j] <= 5 :
            cctvs.append((i,j,arr[i][j]))

CCTV_COUNT = len(cctvs)
min_blank = total_blank

cctv_cover = [[set()] for _ in range(CCTV_COUNT)]
for i in range(CCTV_COUNT) :
    si, sj, num = cctvs[i]
    for watch in CCTV[num] :
        cover = set()
        for direction in watch :
            di, dj = d[direction]
            for k in range(n+m) :
                ni , nj = si + k*di, sj + k*dj
                if 0<=ni<n and 0<=nj<m :
                    if arr[ni][nj] == 6 :
                        break
                    elif arr[ni][nj] == 0 :
                        cover.add((ni,nj))
                else :
                    break
        if cover :
            cctv_cover[i].append(cover)

# print(cctv_cover)
dfs(0, set())
print(min_blank)

