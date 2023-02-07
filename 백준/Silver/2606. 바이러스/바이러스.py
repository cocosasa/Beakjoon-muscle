import sys
input = sys.stdin.readline

def infect(edgearr,n,visited) :
    visited.append(n)
    zombie.add(n)
    for v in edgearr[n] :
        if v not in visited :
            infect(edgearr,v,visited)

N = int(input().strip())
M = int(input().strip())

edge = [[] for _ in range(N+1)]
zombie = {1,}

for i in range(M) :
    a, b = map(int,input().strip().split())
    edge[a].append(b)
    edge[b].append(a)
visited = []
infect(edge,1,visited)

print(len(zombie)-1)
