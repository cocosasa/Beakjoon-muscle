Num = []
for i in range(10) :
    n = int(input())
    Num.append(n%42)

Num = set(Num)
print(len(Num))