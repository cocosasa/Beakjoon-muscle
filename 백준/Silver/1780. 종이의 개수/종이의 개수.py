import sys
input = sys.stdin.readline

def cut(arr, n):
    color = arr[0][0]
    cnt = 1
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            if arr[i][j] == color:
                cnt += 1
    if cnt == n ** 2:
        paper_cnt[color + 1] += 1
        return
    nn = n // 3
    arr_up = arr[:nn]
    arr_mid = arr[nn:2 * nn]
    arr_down = arr[2 * nn:]

    for cut_arr in (arr_up, arr_mid, arr_down):
        cut(list(map(lambda x: x[:nn], cut_arr)), nn)
        cut(list(map(lambda x: x[nn:2 * nn], cut_arr)), nn)
        cut(list(map(lambda x: x[2 * nn:], cut_arr)), nn)
    return


N = int(input())

paper = [list(map(int, input().strip().split())) for _ in range(N)]
paper_cnt = [0, 0, 0]
cut(paper, N)
print(*paper_cnt, sep='\n')
