s_in = list(map(int,input().split()))
asc = list(range(1,9))
des = list(reversed(range(1,9)))
if s_in == asc :
    print('ascending')
elif s_in == des :
    print('descending')
else :
    print('mixed')