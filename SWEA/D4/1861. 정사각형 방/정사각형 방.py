def bfs(si, sj):
    visited = [[0] * N for _ in range(N)]
    Q = [(si, sj)]
    visited[si][sj] = 1
    _max = 0
    while Q:
        i, j = Q.pop(0)
        for di, dj in d:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and nums[ni][nj] == nums[i][j] + 1:

                Q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1

    return visited[i][j]


d = ((-1, 0), (1, 0), (0, 1), (0, -1))

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    nums = [list(map(int, input().split())) for _ in range(N)]
    ansdict = {}
    for i in range(N):
        for j in range(N):
            move = bfs(i, j)
            if ansdict.get(move):
                ansdict[move].append(nums[i][j])
            else:
                ansdict[move] = [nums[i][j]]

    ans2 = max(ansdict.keys())
    ans1 = min(ansdict[ans2])
    print(f'#{tc}', ans1, ans2)
