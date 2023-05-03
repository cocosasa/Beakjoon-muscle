def move_ball(board, blue, red, direction, cnt) :
    global ans
    if ans <= cnt :
        # print('볼 가치 없음!')
        return
    arr = [board[i][:] for i in range(n)]
    blue_pos = blue.copy()
    red_pos = red.copy()
    di, dj = d[direction]

    blue_meet_red = False
    red_meet_blue = False
    
    # 파란 구슬 이동
    while True :
        ni, nj = blue_pos[0] + di, blue_pos[1] + dj
        if arr[ni][nj] == 'O' :
            # print(dir_name[direction], 'blue in hole!')
            return
        elif arr[ni][nj] == '#':
            break
        elif arr[ni][nj] == 'R' :
            # print(dir_name[direction])
            # print('blue meet red')
            blue_meet_red = True
        blue_pos[0], blue_pos[1] = ni, nj

    # 빨간 구슬 이동
    while True :
        ni, nj = red_pos[0] + di, red_pos[1] + dj
        if arr[ni][nj] == 'O' :
            if ans > cnt :
                ans = cnt
            # print(dir_name[direction], 'bead in hole!')
            return
        elif arr[ni][nj] == '#' :
            break
        elif arr[ni][nj] == 'B' :
            # print(dir_name[direction])
            # print('red meet blue')
            red_meet_blue = True
        red_pos[0], red_pos[1] = ni, nj


    # 10번째 시도인데 구멍에 들어가지 않음
    if cnt == 10 :
        # print('10 try!')
        return
    
    # 같은 곳에 있으면 뒤에 있던 구슬을 한칸 뒤로
    if red_pos == blue_pos :
        # print('same pos!')
        if blue_meet_red :
            # print('blue back')
            blue_pos = [blue_pos[0]-di,blue_pos[1]-dj]
        elif red_meet_blue :
            # print('red back')
            red_pos = [red_pos[0]-di,red_pos[1]-dj]

    # 움직이지 않았으면 return
    if blue == blue_pos and red == red_pos :
        # print(dir_name[direction] ,'not moved. return!')
        return
    
    # 위치스위치
    # print('switch!')
    # 여기가 문제
    
    # arr[blue[0]][blue[1]], arr[blue_pos[0]][blue_pos[1]] = arr[blue_pos[0]][blue_pos[1]], arr[blue[0]][blue[1]]
    # arr[red[0]][red[1]],   arr[red_pos[0]][red_pos[1]]   = arr[red_pos[0]][red_pos[1]],   arr[red[0]][red[1]]
    arr[blue[0]][blue[1]], arr[red[0]][red[1]] = '.','.'
    arr[blue_pos[0]][blue_pos[1]], arr[red_pos[0]][red_pos[1]] = 'B', 'R'

    # print(dir_name[direction], cnt)
    # for i in range(n) :
    #     print(*arr[i])
    # print()

    for nd in range(4) :
        # 같은 방향은 다시 시도하지 않음
        if nd == direction :
            continue
        move_ball(arr, blue_pos, red_pos, nd, cnt+1)


d = ((0,1),(1,0),(0,-1),(-1,0))

dir_name = {
    0:'right',
    1:'down',
    2:'left',
    3:'up',
}


n, m = map(int,input().split())

board = [list(input()) for _ in range(n)]

for i in range(n):
    for j in range(m) :
        if board[i][j] == 'B' :
            blue = [i,j]
        elif board[i][j] == 'R' :
            red = [i,j]
ans = 99
for direc in range(4) :
    move_ball(board, blue, red, direc, 1)

if ans == 99:
    ans = -1
print(ans)