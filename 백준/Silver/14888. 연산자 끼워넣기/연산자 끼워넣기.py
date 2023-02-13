from itertools import permutations

N = int(input())

numbers = input().split()

operator = list(map(int, input().split()))
answers = []

op = ['+', '-', '*', '//']
op_list = []
for i in range(4):
    op_list.extend([op[i] for _ in range(operator[i])])

op.clear()
for i in permutations(op_list, N-1):
    op.append(i)
op = list(set(op))

M = len(op)

for i in range(M):
    formula = numbers[0]
    for j in range(1, N):

        if int(formula) < 0 and op[i][j - 1] == '//' and int(numbers[j]) > 0:
            formula = str(-1 * int(formula))
            formula += op[i][j - 1]
            formula += numbers[j]
            formula = str(-1 * eval(formula))
        else:
            formula += op[i][j - 1]
            formula += numbers[j]
            formula = str(eval(formula))

    answers.append(int(formula))

_max = max(answers)
_min = min(answers)
print(_max)
print(_min)
