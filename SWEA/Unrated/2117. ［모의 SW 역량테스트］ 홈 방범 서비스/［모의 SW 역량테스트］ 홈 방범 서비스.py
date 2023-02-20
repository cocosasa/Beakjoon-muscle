import collections


def service(y, x):
    queue = collections.deque()
    house = 0
    queue.append((y, x))
    visited[y][x] = 1
    house_cnt = []
    for K in range(1, 2 * N):
        length = len(queue)
        for i in range(length):
            y, x = queue.popleft()

            if town[y][x] == 1:
                house += 1

            for dy, dx in d:
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] != 1:
                    queue.append((ny, nx))
                    visited[ny][nx] = 1

        profit = house * M - (K ** 2 + (K - 1) ** 2)
        if profit >= 0:
            house_cnt.append(house)
    if house_cnt:

        return max(house_cnt)
    else:
        return 0


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    town = [list(map(int, input().split())) for _ in range(N)]
    _max = 0
    d = ((1, 0), (0, -1), (-1, 0), (0, 1))

    for i in range(N):
        for j in range(N):
            visited = [[0] * N for _ in range(N)]
            tmp = service(i, j)
            if _max < tmp:
                _max = tmp
    print(f'#{tc}', _max)
