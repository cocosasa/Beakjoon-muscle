import sys
input = sys.stdin.readline
N = int(input())

lopes = [int(input()) for i in range(N)]
lopes.sort()
for i in range(N) :
    lopes[i] *= N-i
print(max(lopes))