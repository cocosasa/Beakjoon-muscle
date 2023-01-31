a,b = 2,2
while a!=0 and b!=0 :
    a,b = map(int,input().split())
    if a!=0 or b!=0 :
        print(a+b)