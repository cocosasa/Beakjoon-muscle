n = int(input())
for i in range(1,n+1) :
    print("*"*i+" "*((n-i)*2)+"*"*i)
for i in range(1,n) :
    print("*"*(n-i)+" "*(i*2)+"*"*(n-i))