N = int(input())
A = list(map(int,input().split()))
max = A[0]
min = A[0]
for i in range(1,N):
    if max < A[i] :
        max = A[i] 
    if min > A[i] :
        min = A[i] 

print(min,max)