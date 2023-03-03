N = int(input())
ans = 0
jeong = 0
for i in range(1,N+1) :
    for j in range(1,N+2 - i) :
        tmp = i * j
        if tmp <= N :
            if i == j :
                jeong += 1
            else :
                ans += 1
print( ans//2 + jeong)
