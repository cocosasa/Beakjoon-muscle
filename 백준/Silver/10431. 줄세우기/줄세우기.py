from collections import  deque

T = int(input())

for tc in range(1,T+1) :
    t, *meter = map(int,input().split())

    meter = deque(meter)
    line = [meter.popleft()]
    ans = 0
    for i in range(1,20) :
        line.append(meter.popleft())
        j = i

        while j != 0 and line[j-1] > line[j] :
            line[j - 1], line[j] = line[j], line[j - 1]
            j -= 1
            ans += 1
    if line[0] > line[-1] :
        line[0], line[1] = line[1], line[0]
        ans += 1
    print(tc, ans)

