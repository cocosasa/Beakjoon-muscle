import sys
input = sys.stdin.readline

N = int(input())
sequence = []
stack = []

for i in range(N) :
    sequence.append(int(input()))
answers = []
flag = True
cur = 1

for n in sequence :
    while cur <= n :
        stack.append(cur)
        answers.append('+')
        cur += 1
    
    if n == stack[-1] :
        stack.pop()
        answers.append('-')
    else :
        flag =False
        break
        
if flag :
    for ans in answers :
        print(ans)
else :
    print('NO')