def check_palindrome(s):
    for ㅓ in range(len(s) // 2):
        if s[ㅓ] != s[-ㅓ - 1]:
            return False
    else:
        return True


T = 10

for tc in range(1, T + 1):
    lee = input()
    N = 100
    board = [list(input()) for o in range(N)]
    board_col = list(zip(*board))
    max_length = 1
    for i in range(N):
        for M in range(max_length, 100-i) :
            for j in range(N - M + 1):
                s_row = board[i][j:j+M]
                s_col = board_col[i][j:j+M]

                if check_palindrome(s_row) and max_length < M:
                    max_length = M

                if check_palindrome(s_col) and max_length < M:
                    max_length = M

    print(f'#{tc} {max_length}')