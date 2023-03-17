import sys
sys.setrecursionlimit(10**9)

def recur(a, alen ,blen):
    global done
    if done :
        return True
    reverse_a = a[::-1]
    if a not in B and reverse_a not in B:
        return False 
    if alen == blen:
        if a == B:
            done = True
            return True
        return False
    return recur(a+'A',alen+1, blen) or recur('B' + reverse_a , alen+1,blen )
    


A = input()
B = input()
alen = len(A)
blen = len(B)

done = False

ans = recur(A,alen,blen)

if ans :
    print(1)
else :
    print(0)