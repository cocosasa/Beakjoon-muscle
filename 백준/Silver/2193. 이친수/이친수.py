N = int(input())

Twochin = [0,1,1]
for i in range(3,N+1) :
    Twochin.append(Twochin[i-1] + Twochin[i-2])
print(Twochin[-1])
 