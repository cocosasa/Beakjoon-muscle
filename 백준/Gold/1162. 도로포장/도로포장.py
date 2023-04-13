import heapq
import sys
from sys import maxsize
input = sys.stdin.readline

def dijkstra(u):
    Q = []
    D[u][k] = 0
    heapq.heappush(Q, (0, u, k))

    while Q:
        d, u , cnt = heapq.heappop(Q)

        visited[u][cnt] = 1

        if u == n :
            continue
        if D[u][cnt] < d :
            continue
        for w, v in graph[u]:
            if cnt > 0 and not visited[v][cnt-1]:
                if D[v][cnt-1] > d:
                    D[v][cnt-1] = d
                    heapq.heappush(Q, (d, v, cnt-1))
            if not visited[v][cnt] :
                nw = d + w
                if D[v][cnt] > nw:
                    D[v][cnt] = nw
                    heapq.heappush(Q, (nw, v, cnt))


n, m, k = map(int,input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m) :
    s, g, w = map(int,input().split())
    graph[s].append((w, g))
    graph[g].append((w, s))

visited=[[0]*(k+1) for _ in range(n+1)]
D = [[0]*(k+1)] + [[maxsize] * (k+1) for _ in range(n)]
dijkstra(1)
print(min(D[n]))