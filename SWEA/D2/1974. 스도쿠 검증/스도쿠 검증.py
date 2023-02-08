T = int(input())
 
test_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
 
for test_case in range(1, T + 1):
    arr = []
    box = []
    flag = True
    for i in range(9):
        arr.append(list(map(int, input().split())))
 
    for i in range(9):
        temp = []
        if test_set != set(arr[i]):
            flag = False
            break
        for j in range(9):
            temp.append(arr[j][i])
            box.append(arr[i // 3 * 3 + j // 3][i % 3 * 3 + j % 3])
 
        if test_set != set(temp):
            flag = False
            break
        if test_set != set(box):
            flag = False
            break
 
    if flag:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')