N = int(input())
num = list(int(input()) for _ in range(N))

num.sort()

for i in range(N) :
    print(num[i])