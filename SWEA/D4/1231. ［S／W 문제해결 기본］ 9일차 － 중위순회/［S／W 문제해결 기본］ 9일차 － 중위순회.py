def inorder(v):
    if v <= last:
        inorder(2 * v)
        ans.append(tree[v])

        inorder(2 * v + 1)


T = 10
for tc in range(1, T + 1):
    N = int(input())

    tree = [0]

    last = N
    for i in range(N):
        p, char, *c = input().split()
        tree.append(char)

    ans = []
    inorder(1)
    print(f'#{tc}', ''.join(ans))
