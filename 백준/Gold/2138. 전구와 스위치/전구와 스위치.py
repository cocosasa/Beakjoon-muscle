N = int(input())

start = list(map(int, input()))
target = list(map(int, input()))

start_with_first = start.copy()

ans = [-1]

cnt1 = 0
for i in range(1, N-1):
    if start[i-1] != target[i-1]:
        for j in range(i-1, i+2):
            start[j] = (start[j] + 1) % 2
        cnt1 += 1
if start[N-2] != target[N-2]:
    for j in range(N-2, N):
        start[j] = (start[j] + 1) % 2
    cnt1 += 1

if start == target:
    ans.append(cnt1)

cnt2 = 1
for j in range(0, 2):
    start_with_first[j] = (start_with_first[j] + 1) % 2
for i in range(1, N-1):
    if start_with_first[i-1] != target[i-1]:
        for j in range(i-1, i+2):
            start_with_first[j] = (start_with_first[j] + 1) % 2
        cnt2 += 1
if start_with_first[N-2] != target[N-2]:
    for j in range(N-2, N):
        start_with_first[j] = (start_with_first[j] + 1) % 2
    cnt2 += 1

if start_with_first == target:
    ans.append(cnt2)

if len(ans) == 1:
    print(ans[0])
else:
    ans.sort()
    print(ans[1])
