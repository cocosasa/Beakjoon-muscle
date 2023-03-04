d_dict = {
    0: (-1, 0),
    1: (0, 1),
    2: (1, 0),
    3: (0, -1)
}

C, R = map(int, input().split())

target = int(input())

if C*R < target :
    print(0)
else :
    seat = [[0] * C for _ in range(R)]
    direction = 0
    i = R - 1
    j = 0
    num = 1
    seat[i][j] = num
    num += 1
    while seat[i][j] != target:
        di, dj = d_dict[direction % 4]
        ni, nj = i + di, j + dj
        
        if 0 <= ni < R and 0 <= nj < C and seat[ni][nj] == 0:
            seat[ni][nj] = num
            num += 1
            i = ni
            j = nj
        else:
            direction += 1

    print( j + 1, R - i)
