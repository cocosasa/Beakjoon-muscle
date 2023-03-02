from itertools import combinations

N = int(input())
people = list(range(N))
adj_matrix = [list(map(int,input().split())) for _ in range(N)]
combi = list(map(set,combinations(people,N//2)))

_min = 99999999

for com in combi :
    team1 = list(com)
    team2 = list(set(people)-com)
    team1_synergy = 0
    team2_synergy = 0
    for i in team1 :
        for person in team1 :
            if person == i :
                continue
            team1_synergy += adj_matrix[i][person]
    for i in team2:
        for person in team2 :
            if person == i :
                continue
            team2_synergy += adj_matrix[i][person]

    cal = abs(team1_synergy - team2_synergy)
    if _min > cal :
        _min = cal
print(_min)
