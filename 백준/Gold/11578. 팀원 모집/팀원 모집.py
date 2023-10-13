import sys
input = sys.stdin.readline

N, M = map(int, input().split())

bit = (1 << N) -1
ans = M + 1

student = []
for i in range(M):
    solve = 0
    solve_list = list(map(int, input().split()[1:]))
    for num in solve_list:
        solve |= (1 << (num-1))
    student.append(solve)
for i in range((1 << M)-1):
    trybit = 0
    count = 0
    for j in range(M):
        if(count >= ans) : 
            break
        if i & (1 << j):
            trybit |= student[j]
            count += 1
    if trybit == bit:
        ans = min(ans, count)
if(ans == M +1) :
    print(-1)
else : 
    print(ans)
