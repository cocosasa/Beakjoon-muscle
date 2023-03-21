from collections import deque

N, K = map(int, input().split())

negoo = list(map(int, input().split()))

belt = deque()

for i in range(2*N):
    belt.append([0, negoo[i]])

broke = 0

time = 0

while broke < K:
    belt.rotate(1)
    belt[N-1][0] = 0
    for i in range(N-2, -1, -1):
        if belt[i][0] == 1 and belt[i+1][0] == 0 and belt[i+1][1] > 0:
            belt[i][0] = 0
            belt[i+1][0] = 1
            belt[i+1][1] -= 1

    belt[N-1][0] = 0
    if belt[0][1] > 0:
        belt[0][0] = 1
        belt[0][1] -= 1
    broke = 0
    for i in range(2*N):
        if belt[i][1] == 0:
            broke += 1
    time += 1

print(time)
