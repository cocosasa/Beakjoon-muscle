import sys
input = sys.stdin.readline

n = int(input())

nums = [int(input()) for i in range(n)]

d=[0]*10000
d[0]=nums[0]
if n > 1 :
    d[1]=nums[0]+nums[1]
if n > 2 :
    d[2]=max(d[1], nums[2]+nums[0], nums[2]+nums[1])

for i in range(3,n):
    d[i]=max(d[i-1], nums[i]+d[i-2], nums[i]+nums[i-1] + d[i-3])


print(d[n-1])