N = int(input())
ox = []
Combo = 1
Score = []
for i in range(N) :
    ox.append(input())
    Score.append(0)
for i in range(N) :
    stri = ox[i]
    Combo = 1
    Score[i] = 0
    if stri[0] == "O" :
        Score[i] += 1
    for j in range(1,len(ox[i])) :
        if stri[j-1] == "X" and stri[j] == "O" :
            Score[i] += Combo
        elif stri[j-1] == "O" and stri[j] == "O" :
            Combo +=1
            Score[i] += Combo
        elif stri[j] == "X" :
            Combo = 1
for i in range(N) :
    print(Score[i])