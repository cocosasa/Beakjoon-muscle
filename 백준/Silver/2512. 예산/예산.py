N = int(input())

yeahsan = list(map(int, input().split()))

budget = int(input())

top = max(yeahsan)
bottom = 0
if sum(yeahsan) >= budget:
    # 이분탐색해보자
    while top >= bottom:
        limit = (top + bottom) // 2
        total = 0
        for b in yeahsan:
            total += min(limit, b)

        if total <= budget:
            bottom = limit + 1
        else:
            top = limit - 1

print(top)
