def toint(c):
    if c.isdigit():
        return int(c)
    return c
def postorder_cal(v):
    if tree[v][1] != 0:
        return op_cal[tree[v][0]](postorder_cal(tree[v][1]), postorder_cal(tree[v][2]))
    return tree[v][0]
op_cal = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
}
for tc in range(1, 11):
    N = int(input())
    tree = [[0] * 3 for _ in range(N + 1)]
    for i in range(1, N + 1):
        n, data, *child = map(toint, input().split())
        v = tree[i]
        v[0] = data
        if child:
            v[1] = child[0]
            v[2] = child[1]
    print(f'#{tc} {postorder_cal(1):.0f}')
