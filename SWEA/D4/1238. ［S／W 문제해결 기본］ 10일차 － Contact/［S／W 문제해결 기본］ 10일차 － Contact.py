def bfs(s) :
    visited = [0]*101
    Q = [s]
    visited[s] = 1
    while Q :
        v = Q.pop(0)
        for w in adjL[v] :
            if visited[w] == 0 :
                Q.append(w)
                visited[w] = visited[v] + 1
    _max = max(visited)
    return 100-visited[::-1].index(_max)


T = 10
for tc in range(1,T+1) :
    N, start = map(int,input().split())
    adjL = [[] for _ in range(100+1)]
    contact = list(map(int,input().split()))

    for i in range(N//2) :
        s, e = contact[i*2], contact[i*2+1]
        adjL[s].append(e)

    ans = bfs(start)
    print(f'#{tc}',ans)