n, m, k = map(int,input().split())

fire = dict()

d = ((-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1))
split_fire = { 0:(0,2,4,6), 1:(1,3,5,7) }
for _ in range(m) :
    i, j, weight, speed, direction = map(int,input().split())
    i, j = i-1, j-1
    di, dj = d[direction]
    ni = (i + speed * di)%n
    nj = (j + speed * dj)%n
    if fire.get((ni,nj)) :
        fire[(ni,nj)].append((weight, speed, direction))
    else :
        fire[(ni,nj)] = [(weight, speed, direction)]

for _ in range(k) :
    next = dict()
    for (si, sj), lst in fire.items():
        total_weight = 0
        total_speed = 0
        is_same = 0
        fireball_count = 0
        # check direction
        for weight, speed, direction in lst :
            total_weight+=weight
            total_speed+=speed
            is_same += direction%2
            fireball_count += 1

        if fireball_count > 1:
            weight = total_weight//5
            if not weight :
                continue
            speed = total_speed // fireball_count
            if not is_same or is_same == fireball_count :
                is_same = 0
            else :
                is_same = 1
            for direction in split_fire[is_same] :
                di, dj = d[direction]
                ni = (si + speed * di)%n
                nj = (sj + speed * dj)%n
                if next.get((ni,nj)) :
                    next[(ni,nj)].append((weight, speed , direction))
                else :
                    next[(ni,nj)] = [(weight, speed, direction)]
        else :
            di, dj = d[direction]
            ni = (si + speed * di)%n
            nj = (sj + speed * dj)%n
            if next.get((ni,nj)) :
                next[(ni,nj)].append((weight, speed , direction))
            else :
                next[(ni,nj)] = [(weight, speed, direction)]
    fire = next

total_weight = 0
for lst in fire.values():
    for weight, speed, direction in lst :
        total_weight+=weight
        
print(total_weight)
