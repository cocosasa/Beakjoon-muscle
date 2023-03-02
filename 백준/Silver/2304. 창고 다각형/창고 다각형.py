N = int(input())

support = [list(map(int,input().split())) for _ in range(N)]
_max = 0
_max_idx = 0
_max_range = 0
for L, H in support :
    if L > _max_range :
        _max_range = L
    if _max < H :
        _max = H
        _max_idx = L
arr = [0] * (_max_range+1)
for L, H in support :
    arr[L] = H
_sum = 0
_max_tmp = arr[0]
for i in range(_max_idx) :
    if arr[i] > _max_tmp :
        _max_tmp = arr[i]
    _sum += _max_tmp

_max_tmp = arr[-1]
for i in range(_max_range,_max_idx-1,-1) :
    if arr[i] > _max_tmp :
        _max_tmp = arr[i]
    _sum += _max_tmp

print(_sum)