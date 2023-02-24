import sys
input = sys.stdin.readline

string = list(input().strip())

N = int(input())
tmp = []
for i in range(N) :
    commend, *c = input().split()

    if commend == 'L' :
        if string :
            tmp.append(string.pop())
    elif commend == 'D' :
        if tmp :
            string.append(tmp.pop())
    elif commend == 'B' :
        if string :
            string.pop()
    else :
        string.extend(c)

while tmp :
    string.append(tmp.pop())

print(''.join(string))