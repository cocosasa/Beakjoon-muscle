arr = [0]*10001
for i in range(1, 10001) :
    n = i
    while n < 10001 : 
        n = n + sum(map(int,str(n)))
        # print(n)
        if n > 10000 or arr[n]:
            break
        arr[n] = 1

for i in range(1, 10001) :
    if not arr[i] :
        print(i)