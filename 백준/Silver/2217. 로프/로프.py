N = int(input())
lopes = [int(input()) for _ in range(N)]
lopes.sort()
for i in range(N) :
    lopes[i] *= N-i
print(max(lopes))