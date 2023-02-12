import sys
input = sys.stdin.readline

N = int(input())

commends = list(input().strip().split() for _ in range(N))
arr = []
dlen = 0
for c in commends :
    cmd = c[0]
    
    if cmd == 'push_front' :
        arr.insert(0, c[1])
        dlen+=1
    elif cmd == 'push_back' :
        arr.append(c[1])
        dlen+=1
    elif cmd == 'pop_front' :
        if dlen > 0 :
            print(arr.pop(0))
            dlen -= 1
        else :
            print(-1)
    elif cmd == 'pop_back' :
        if dlen > 0 :
            print(arr.pop())
            dlen -= 1
        else :
            print(-1)
    elif cmd == 'size' :
        print(dlen)
    elif cmd == 'empty' :
        if dlen:
            print(0)
        else :
            print(1)
    elif cmd == 'front' :
        if dlen :
            print(arr[0])
        else :
            print(-1)
    elif cmd == 'back' :
        if dlen :
            print(arr[-1])
        else :
            print(-1)