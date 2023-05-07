from collections import deque
from sys import maxsize
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(n-1) :
    p, q, r = map(int,input().split())

    graph[p].append((r, q))
    graph[q].append((r, p))


for _ in range(m) :
    k, video = map(int, input().split())
    
    visited = [0] * (n+1)
    visited[video] = 1
    ans = 0

    Q = deque()
    Q.append((video, maxsize))

    while Q : 
        v, w  = Q.popleft()
        for nw, nv in graph[v]:
            if not visited[nv] :
                usado = min(w, nw)
                if usado >= k  :
                    Q.append((nv, usado))
                    ans += 1
                    visited[nv] = 1
    print(ans)
