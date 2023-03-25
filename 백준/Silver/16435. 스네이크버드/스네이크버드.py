N ,L = map(int,input().split()) 

fruits = list(map(int,input().split()))

fruits.sort()
for i in range(N) :
    if fruits[i] <= L :
        L+= 1
print(L)