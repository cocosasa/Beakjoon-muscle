import sys
arrinput = list(map(int,sys.stdin.readline().split()))
nsum = 0
for n in arrinput :
	nsum += n ** 2
ans = nsum%10
print(ans)