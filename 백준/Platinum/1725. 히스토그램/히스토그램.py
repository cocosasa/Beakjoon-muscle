import sys; input = sys.stdin.readline

n = int(input())



arr = [int(input()) for _ in range(n)]
ans = 0

stack = []
for i in range(n) :
    idx = i
    while stack and stack[-1][1] > arr[i] :
        idx, num = stack.pop()
        # 사각형 만들어보고 값 갱신
        ans = max(ans,(i-idx) * num)
    stack.append((idx, arr[i]))

while stack :
    # 나머지로 사각형 만들기
    idx, num = stack.pop()
    ans = max(ans, (n-idx)*num)
print(ans)
