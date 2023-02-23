def toint(c) :
    if c.isdigit() :
        return int(c)
    return c

def postorder_cal(v) :
    if tree[v][1] != 0 :
        op = tree[v][0]
        val1 = postorder_cal(tree[v][1])
        val2 = postorder_cal(tree[v][2])

        if op == '+' :
            return val1 + val2
        elif op == '-' :
            return val1 - val2
        elif op == '/' :
            return val1 / val2
        elif op == '*' :
            return val1 * val2
    return tree[v][0]

T = 10

for tc in range(1,T+1) :
    N = int(input())
    tree = [[0]*3 for _ in range(N+1)]
    for i in range(1,N+1) :
        info = list(map(toint,input().split()))

        tree[i][0] = info[1]
        if len(info) > 2 :
            tree[i][1] = info[2]
            tree[i][2] = info[3]

    ans = postorder_cal(1)
    print(f'#{tc} {ans:.0f}')