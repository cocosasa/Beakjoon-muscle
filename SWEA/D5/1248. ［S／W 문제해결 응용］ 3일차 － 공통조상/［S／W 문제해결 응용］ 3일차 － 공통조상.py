def postorder(v):
    global ans
    if tree[v][1] != 0:
        left = postorder(tree[v][0])
        right = postorder(tree[v][1])
        if g1 in left and g2 in right or g2 in left and g1 in right:
            ans = v, len(left + right + [v])
        return left + right + [v]
    elif tree[v][0] != 0:
        left = postorder(tree[v][0])
        return left + [v]
    else:
        return [v]


T = int(input())

for tc in range(1, T + 1):
    V, E, g1, g2 = map(int, input().split())

    tree = [[0] * 2 for _ in range(V + 1)]
    temp = list(map(int, input().split()))
    for i in range(E):
        p, c = temp[i * 2], temp[i * 2 + 1]

        if tree[p][0] == 0:
            tree[p][0] = c
        else:
            tree[p][1] = c
    ans = 0

    history = postorder(1)
    print(f'#{tc}', *ans)