import sys; input = sys.stdin.readline

while True :
    his_toe_gram = list(map(int,input().split()))
    if his_toe_gram == [0] :
        break

    n , *his_toe_gram = his_toe_gram
    st = [0]*(4*n)

    arr = his_toe_gram
    ans = 0
    # build(1, 0, n-1)
    # print(ans)

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
