import heapq
import sys
input = sys.stdin.readline
from collections import deque


def dijkstra(u):
    Q = []
    D[u] = 0
    heapq.heappush(Q, (0, u))

    while Q:
        d, u = heapq.heappop(Q)
        if D[u] < d :
            continue
        for p, v in graph[u]:
            if shortest_path[u][v]:
                continue
            nw = D[u] + p
            if D[v] > nw:
                D[v] = nw
                heapq.heappush(Q, (nw, v))

def BFS(g) :
    Q = deque()
    Q.append(g)
    visited[g][g] = 1
    while Q :
        g = Q.popleft()
        if g == start:
            continue
        for p, s in graph_reverse[g] :
            if D[g] == D[s] + p and not visited[s][g]:
                Q.append(s)
                visited[s][g] = 1
                shortest_path[s][g] = 1


while True:
    N, M = map(int, input().split())
    if not N and not M:
        break
    start, goal = map(int, input().split())

    graph = [[] for _ in range(N)]
    graph_reverse = [[] for _ in range(N)]
    shortest_path = [[0]*N for _ in range(N)]
    for _ in range(M):
        u, v, p = map(int, input().split())
        graph[u].append((p,v))
        graph_reverse[v].append((p,u))
    inf = 10**9
    D = [inf]*(N)
    dijkstra(start)
    visited=[[0]*N for _ in range(N)]
    BFS(goal)
    D = [inf]*(N)
    dijkstra(start)

    if D[goal] == inf:
        print(-1)
    else:
        print(D[goal])
