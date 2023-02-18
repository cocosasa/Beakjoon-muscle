from itertools import permutations

k = int(input())

boo = input().split()

numbers = [0,1,2,3,4,5,6,7,8,9]

pm = permutations(numbers,k+1)

ans_list = []
for p in pm :
    for i in range(k):
        if boo[i] == '<' :
            if p[i] < p[i+1] :
                continue
            else :
                break
        else :
            if p[i] > p[i+1] :
                continue
            else :
                break
    else :
        ans_list.append(p)
ans_list.sort()
_max = max(ans_list)
_min = min(ans_list)

print(*_max, sep='')
print(*_min,sep='')