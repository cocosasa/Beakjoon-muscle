A = int(input())
B = int(input())
C = int(input())

Multi_Num = A * B * C

NumCount = [0,0,0,0,0,0,0,0,0,0]
Numlength = len(str(Multi_Num))
Numstr = str(Multi_Num)

for i in range(0,Numlength) :
    K = int(Numstr[i])
    NumCount[K] += 1
for i in range(0,10) :
    print(NumCount[i])
    