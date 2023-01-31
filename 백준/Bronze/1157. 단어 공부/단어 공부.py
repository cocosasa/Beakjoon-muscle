arrstr = input()

alpha= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
arrstr = arrstr.upper()
arrcnt = []
for c in alpha :
    arrcnt.append(arrstr.count(c))
sorted_arrcnt = sorted(arrcnt)
if sorted_arrcnt[-1] == sorted_arrcnt[-2] :
    print('?')
else :
    ans = arrcnt.index(sorted_arrcnt[-1])
    print(alpha[ans])