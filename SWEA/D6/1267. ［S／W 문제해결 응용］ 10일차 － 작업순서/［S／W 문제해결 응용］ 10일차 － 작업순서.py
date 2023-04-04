def dfs(v):
    global founded, cnt
    path.append(v)
    visited[v] = 1
    cnt -= 1
    if cnt == 0:
        founded = True
    if founded:
        return

    for w in adj_matrix[v]:
        if founded:
            return
        if visited[w] == 0:
            pre_task[w] -= 1
            if not pre_task[w]:
                dfs(w)

T = 10

for tc in range(1, T+1):
    V, E = map(int, input().split())

    tmp = list(map(int, input().split()))

    adj_matrix = [[] for _ in range(V+1)]

    visited = [0] * (V+1)
    founded = False

    pre_task = [0]*(V+1)
    for i in range(0, 2*E, 2):
        s, g = tmp[i], tmp[i+1]

        adj_matrix[s].append(g)
        pre_task[g] += 1

    cnt = V

    start_task = []
    # 시작 작업
    for i in range(1, V+1):
        if not pre_task[i]:
            start_task.append(i)

    path = []
    for i in start_task:
        dfs(i)

    print(f'#{tc}', *path)