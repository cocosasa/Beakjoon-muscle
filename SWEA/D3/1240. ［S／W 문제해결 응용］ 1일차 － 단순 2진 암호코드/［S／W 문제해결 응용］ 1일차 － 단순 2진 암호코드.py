T = int(input())

hard_dict = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
    '0000000': 0

}

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    code = [input() for _ in range(N)]
    row = 1
    while code[row] == '0' * M:
        row += 1
    col = M - 1
    while code[row][col] != '1':
        col -= 1

    encode = []
    length = (col + 1) // 7
    for i in range(length):
        tmp = code[row][col - (i + 1) * 7 + 1:col - i * 7 + 1]
        encode.append(tmp)

    data = 0
    ans = 0
    for i in range(len(encode)):
        ans += hard_dict[encode[i]]
        if i % 2:
            data += hard_dict[encode[i]] * 3
        else:
            data += hard_dict[encode[i]]
    if data % 10:
        ans = 0
    print(f'#{tc} {ans}')
