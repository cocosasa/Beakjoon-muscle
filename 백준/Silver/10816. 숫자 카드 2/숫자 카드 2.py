from collections import Counter
import sys
input = sys.stdin.readline
N = int(input().strip())

Narr = list(map(int,input().strip().split()))
M = int(input())
Marr = list(map(int,input().strip().split()))

cnts = Counter(Narr)
for m in Marr :
    if cnts.get(m) :
        print(cnts[m],end=' ')
    else :
        print(0,end=' ')
