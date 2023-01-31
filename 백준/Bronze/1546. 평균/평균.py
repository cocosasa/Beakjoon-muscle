N = int(input())
avr = []
Score = list(map(int,input().split()))

for i in range(len(Score)) :
    avr.append(Score[i]/max(Score))
print(sum(avr)/N*100)