import sys
input = sys.stdin.readline
N = int(input())
arr_stack = []
for _ in range(N) :
    commend = list(input().split())
    
    if commend[0] == 'push' :
        arr_stack.append(commend[1])
    if commend[0] == 'pop' :
        if len(arr_stack) != 0 :
            print(arr_stack.pop())
        else : 
            print(-1)
    if commend[0] == 'empty' :
        if len(arr_stack) != 0 :
            print(0)
        else :
            print(1)
    if commend[0] == 'size' :
        print(len(arr_stack))
    if commend[0] == 'top' :
        if len(arr_stack) != 0 :
            print(arr_stack[-1])
        else :
            print(-1)
                         