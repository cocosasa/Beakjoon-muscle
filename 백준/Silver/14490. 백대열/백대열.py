def gcd(a, b) :
    while a % b != 0: a, b = b, a % b
    return b

n, m = map(int,input().split(':'))

g = gcd(n, m)
print(str(n//g)+':'+str(m//g))