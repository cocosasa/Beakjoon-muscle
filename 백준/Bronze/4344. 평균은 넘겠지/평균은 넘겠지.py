N = int(input())
avr = []
score = []
ratio = []
count = 0
for i in range(N) :
    score = list(map(int,input().split()))
    avr.append(0)
    ratio.append(0)
    avr[i] = (sum(score)-score[0])/(len(score)-1)
    for j in range(1,len(score)) :
        if score[j] > avr[i] :
            count += 1
    ratio[i] = float((count/(len(score)-1))*100)
    count = 0
for i in range(N):
    ratiti = ratio[i]
    print("%.3f" %(ratiti)+"%")
