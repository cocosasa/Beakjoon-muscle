from collections import deque

n , k = map(int,input().split())


Q = deque()
visited = [0] * 111111
Q.append(n)
visited[n] = 1
while Q :
    now = Q.popleft()
    if now == k :
        break
    for plus in (-1,1,now) :
        nxt = now + plus
        if 0<= nxt <111111 and not visited[nxt]:
            Q.append(nxt)
            visited[nxt] = visited[now] + 1
print(visited[k]-1)
