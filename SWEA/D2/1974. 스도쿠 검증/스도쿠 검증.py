T = int(input())

test_arr = [1,2,3,4,5,6,7,8,9]

for test_case in range(1, T + 1):
    arr = [] 
    tempbox = []
    isgood = True
    for i in range(9) :
        arr.append(list(map(int,input().split())))
    print(f'#{test_case}',end=" ")
    for i in range(9) :
        temp = []
        if set(test_arr) != set(arr[i]) :
                isgood = False
        for j in range(9) :
            
            temp.append(arr[j][i])
            tempbox.append(arr[i%3*3 + j//3 ][i%3*3 + j%3])
            
        if set(test_arr) != set(temp) :
            isgood = False
        if  set(test_arr) != set(tempbox)  :
            isgood = False

    if isgood :
        print("1")
    else :
        print("0")
