def check(ni, nj) :
    if 0 > ni or ni >= N or 0 > nj or nj >= M :
        return True
    return False

N, M = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]

tetromino_1 = [
    ((0,0),(0,1),(0,2),(0,3)),
    ((0,0),(1,0),(2,0),(3,0))
]
tetromino_2 = [
    ((0,0),(0,1),(1,0),(1,1))
]
tetromino_3 = [
    ((0,0),(1,0),(2,0),(2,1)),
    ((0,0),(1,0),(2,0),(2,-1)),
    ((0,0),(0,1),(1,1),(2,1)),
    ((0,0),(0,1),(1,0),(2,0)),
    ((0,0),(-1,0),(0,1),(0,2)),
    ((0,0),(1,0),(0,1),(0,2)),
    ((0,0),(0,1),(0,2),(-1,2)),
    ((0,0),(0,1),(0,2),(1,2))
]
tetromino_4 = [
    ((0,0),(1,0),(1,1),(2,1)),
    ((0,0),(1,0),(1,-1),(2,-1)),
    ((0,0),(0,1),(-1,1),(-1,2)),
    ((0,0),(0,1),(1,1),(1,2))
]
tetromino_5 = [
    ((0,0),(0,-1),(1,0),(0,1)),
    ((0,0),(-1,0),(1,0),(0,1)),
    ((0,0),(0,-1),(-1,0),(0,1)),
    ((0,0),(0,-1),(1,0),(-1,0)),
]
tetro_brute = [tetromino_1,tetromino_2,tetromino_3,tetromino_4,tetromino_5]

_max = 0
for i in range(N) :
    for j in range(M) :
        for tetromino in tetro_brute :
            for tetro in tetromino :
                tmp = 0
                for di, dj in tetro :
                    ni, nj = i + di, j + dj
                    if check(ni, nj) :
                        continue
                    tmp += arr[ni][nj]
                _max = max(_max,tmp)
print(_max)