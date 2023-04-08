import sys 
from collections import Counter
input = sys.stdin.readline

N = int(input())

number = [int(input()) for _ in range(N)]
number.sort()

counter = Counter(number)
most_nums = counter.most_common(2)
most_number = [x[0] for x in most_nums if x[1] == most_nums[0][1]]
most_number.sort()

ans1 = sum(number)/N
if -0.5 < ans1 < 0.5 :
    print(0)
else :
    print(f'{ans1:.0f}')
print(number[N//2])
if len(most_number) == 1 :
    print(most_number[0])
else :
    print(most_number[1])
print(number[-1] - number[0])
