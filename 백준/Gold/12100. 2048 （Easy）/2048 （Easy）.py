import copy

def x_reverse(board):
    return [row[::-1] for row in board]

def trans(board) :
    return [list(row) for row in zip(*board)]

def move(board, cnt) :
    global max_val
    new_board = []
    
    for r in board:
        # 0을 지움
        row = r[:]
        row = [n for n in row if n]
        for i in range(len(row)-1) :
            if row[i] == row[i+1] :
                row[i] *= 2
                row[i+1] = 0
        row = [n for n in row if n]
        new_board.append(row + [0]*(N-len(row)))

    # print(*new_board, sep='\n')
    # print()

    # 깊이 체크 & 최댓값
    if cnt == 5:
        for i in range(N) :
            max_val = max(max_val,max(new_board[i]))
        return
    
    # 왼쪽
    move(copy.deepcopy(new_board), cnt+1)

    # 오른쪽
    move(x_reverse(new_board), cnt+1)

    # 위
    move(trans(new_board), cnt+1)

    # 아래
    move(x_reverse(trans(new_board)), cnt+1)
    

N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]

max_val = 0

move(copy.deepcopy(arr), 1)

move(x_reverse(arr), 1)

move(trans(arr), 1)

move(x_reverse(trans(arr)), 1)

print(max_val)