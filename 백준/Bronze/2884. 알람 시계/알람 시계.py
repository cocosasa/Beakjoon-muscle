a,b = map(int,input().split())
b -= 45
if b < 0 :
    a -= 1
    b = 60 + b

if a<0 : 
    a = 23
print( str(a) +" "+ str(b))