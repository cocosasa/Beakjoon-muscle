a = int(input())
o = 1000 - a
coin = [500,100,50,10,5,1]
count = 0
for j in coin :
    if o == 0 :
        break
    while o >= j and o != 0:
        o-=j
        count += 1
print(count)
