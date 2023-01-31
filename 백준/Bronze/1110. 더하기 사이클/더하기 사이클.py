N = int(input())
M = N
New = 0 
Count = 0
while New != N :
    if N == 0 :
        Count += 1
        break
    Plus = (M % 10) + (M // 10)
    New = (M % 10)*10 + (Plus % 10)
    M = New
    Count += 1
if Count == 0 :
    Count = 1
print(Count)

