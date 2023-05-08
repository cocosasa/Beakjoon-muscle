from heapq import heappop, heappush
import sys; input = sys.stdin.readline

n = int(input())
q = []
total = 0
for _ in range(n) :
    heappush(q,int(input()))
while len(q) != 1 :
    plus = heappop(q) + heappop(q)
    total += plus
    heappush(q, plus)

print(total)