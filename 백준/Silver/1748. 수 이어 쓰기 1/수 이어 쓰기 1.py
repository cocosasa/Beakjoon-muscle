N = int(input())
ans = 0 
powpow = 10
while powpow>1 :
    if 10**(powpow-1)<= N < 10 ** powpow :
        ans += (powpow) * (N - 10**(powpow-1)+1)
        N = 10**(powpow-1)-1
    powpow -= 1
ans += N
print(ans)
    