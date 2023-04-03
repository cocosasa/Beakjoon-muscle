dice = list(map(int,input().split()))
dice.sort()
prize = 0
if dice[0] == dice[1] and dice[1] == dice[2] :
    prize = 10000 + dice[1] * 1000
elif dice[0] == dice[1] or dice[1] == dice[2] :
    prize = 1000 + dice[1] * 100
else :
    prize = dice[2] * 100
    
print(prize)