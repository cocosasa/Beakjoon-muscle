from itertools import combinations

N = int(input())
people = list(range(N))
adj_matrix = [list(map(int, input().split())) for _ in range(N)]

combi_lst = list(combinations(people, N // 2))

_min = 9999
# com : 조합 and 팀 1
for team1 in combi_lst[:len(combi_lst) // 2]:   
    team2 = list(set(people) - set(team1))    #
    team1_synergy = 0
    team2_synergy = 0
    # 
    for player in team1:
        for person in team1:
            team1_synergy += adj_matrix[player][person] 
    for player in team2:        
        for person in team2:
            team2_synergy += adj_matrix[player][person]

    cal = abs(team1_synergy - team2_synergy)

    if _min > cal:
        _min = cal
        if _min == 0 :
            break
print(_min)
