def make_hooi(formula):
    hooi = ''
    for x in formula:
        if x.isdigit():
            hooi += x
        elif x == '(':
            stack.append(x)
        elif x == ')':
            while stack[-1] != '(':
                hooi += stack.pop()
            stack.pop()
        elif icp[x] > isp[stack[-1]]:
            stack.append(x)
        else:
            while isp[stack[-1]] > icp[x]:
                hooi += stack.pop()
            stack.append(x)
    return hooi


def calc_hooi(formula):
    for x in formula:
        if x.isdigit():
            stack.append(int(x))
        else:
            a, b = stack.pop(), stack.pop()
            if x == '+':
                stack.append(b + a)
            elif x == '*':
                stack.append(b * a)
    return stack.pop()


for tc in range(1, 11):
    N = int(input())
    formula = input()

    icp = {'+': 1, '*': 2, '(': 3}
    isp = {'+': 1, '*': 2, '(': 0}

    stack = []

    hoooi = make_hooi(formula)

    answer = calc_hooi(hoooi)

    print(f'#{tc} {answer}')
