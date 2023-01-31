import math
N = int(input())
A = list(map(int,input().split()))
B ,C = map(int,input().split())
answer = 0
for i in range(N) :
    if A[i]<=B :
        answer += 1
    else:
        Div = (A[i]-B)/C
        answer += math.ceil(Div)+1 
print(answer)
 