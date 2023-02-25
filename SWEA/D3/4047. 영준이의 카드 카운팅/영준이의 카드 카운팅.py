T = int(input())
mark_dict = {'S': 0,
             'D': 1,
             'H': 2,
             'C': 3,
             }
for tc in range(1, T + 1):
    card = list(input().strip())
    flag = ''
    have = [[1] * 13 for _ in range(4)]
    while card:
        mark = card[0]
        num = int(''.join(card[1:3]))-1
        card = card[3:]
        if have[mark_dict[mark]][num]:
            have[mark_dict[mark]][num] = 0
        else:
            flag = 'ERROR'
            break
    if flag:
        print(f'#{tc}', flag)
    else:
        ans = [0]*4
        for i in range(4):
            ans[i] = sum(have[i])
        print(f'#{tc}', *ans)