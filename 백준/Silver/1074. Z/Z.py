def rec(n,r,c,cnt) :
    m = (2**(n-1))**2
    mid = (2**n )/2
    if n == 1 :
        if r == 0 and c == 0 :
            return cnt 
        elif r == 0 and c == 1 :
            return cnt + 1
        elif r == 1 and c == 0 :
            return cnt + 2
        elif r == 1 and c == 1 :
            return cnt + 3
    if r < mid:
        if c < mid :
            ans  = rec(n-1,r,c,cnt)
        else :
            ans  = rec(n-1,r,c-mid,cnt+m)
    else :
        if c < mid :
            ans  = rec(n-1,r-mid,c,cnt+2*m)
        else :
            ans  = rec(n-1,r-mid,c-mid,cnt+3*m)
    
    return ans
N, r, c = map(int,input().split())


ans = rec(N,r,c,0)
print(ans)