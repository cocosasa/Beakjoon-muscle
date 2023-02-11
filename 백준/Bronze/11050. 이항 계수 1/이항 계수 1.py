N , K = map(int,input().split())

arr = [[1,1]]
for i in range(N) :
    new = arr[i].copy()
    for j in range(1,len(arr[i])) :
        new[j] += arr[i][j-1]
    new.append(1)
    arr.append(new)
        
print(arr[N-1][K])