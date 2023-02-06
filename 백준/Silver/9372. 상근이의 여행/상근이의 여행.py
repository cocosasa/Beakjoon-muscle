from collections import deque
import sys
input = sys.stdin.readline
def travel(edgearr,n,visited) :
    queue = deque([n])
    visited[n] = True
    
    while queue :
        v = queue.popleft()
        path.append(v)
        
        for i in edgearr[v] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True


T = int(input())
for tc in range(T) :
    N, M = map(int,input().split())
    edge = {}
    visited = [False]*(N+1)
    path = []
    for i in range(M) :
        start, end = map(int,input().strip().split())
        if edge.get(start) :
            edge[start].append(end)
        else :
            edge[start] = [end]
        if edge.get(end) :
            edge[end].append(start)
        else :
            edge[end] = [start]
        
    travel(edge,1,visited)
    print(len(path)-1)
    