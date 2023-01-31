N , M = map(list,input().split())
N = reversed(N)
M = reversed(M)
N = int(''.join(N))
M = int(''.join(M))
if N > M :
    print(N)
else  :
    print(M)