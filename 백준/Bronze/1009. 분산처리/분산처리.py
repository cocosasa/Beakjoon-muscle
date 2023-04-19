
T = int(input())

for t in range(T):
    a, b = map(int, input().split())
    if b == 0 :
        print(1)
    else :
        a %= 10
        if a == 1 or a == 5 or a == 6 :
            print(a)
        elif a == 0 :
            print(10)
        elif a==4 or a==9 :
            b %= 2
            if b : 
                print(a)
            else :
                print((a**2)%10)
        else :
            b %= 4
            if b == 0 :
                print(a**4%10)
            else :
                print(a**b%10)
