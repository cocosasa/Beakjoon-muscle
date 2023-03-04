player = [list(map(int, input().split())) for _ in range(5)]

mc = []
for i in range(5):
    mc.extend(list(map(int, input().split())))

row_bingo = [5] * 5
col_bingo = [5] * 5

cross_bingo = [5] * 2
ans = 0
bingo = 3
victory = False

row_bingo_flag = [True]*5
col_bingo_flag = [True]*5
cross1_bingo = True
cross2_bingo = True
for num in mc:
    if victory:
        break
    ans += 1
    for i in range(5):
        if victory:
            break
        for j in range(5):
            # 그 숫자 일 때
            if num == player[i][j]:
                # 그 위치의 행의 숫자 -1
                row_bingo[i] -= 1
                # 빙고 체크
                if row_bingo_flag[i] and row_bingo[i] == 0:
                    bingo -= 1
                    row_bingo_flag[i] = False

                # 그 위치의 열의 숫자 -1
                col_bingo[j] -= 1
                # 빙고 체크
                if col_bingo_flag[j] and col_bingo[j] == 0:
                    bingo -= 1
                    col_bingo_flag[j] = False
                
                # 대각선 체크
                if i == 2 and j == 2:   # 가운데일 때
                    cross_bingo[0] -= 1
                    cross_bingo[1] -= 1
                    if cross1_bingo and cross_bingo[0] == 0:
                        bingo -= 1
                        cross1_bingo = False
                    if cross2_bingo and cross_bingo[1] == 0:
                        bingo -= 1
                        cross2_bingo = False
                elif i == j:   # 역 슬래시 방향
                    cross_bingo[0] -= 1
                    if cross1_bingo and cross_bingo[0] == 0:
                        bingo -= 1
                        cross1_bingo = False
                elif 4 - i == j:  # 슬래시 방향
                    cross_bingo[1] -= 1
                    if cross2_bingo and cross_bingo[1] == 0:
                        bingo -= 1
                        cross2_bingo = False
                # 3줄 빙고
                if bingo <= 0:
                    victory = True
                    break
print(ans)
