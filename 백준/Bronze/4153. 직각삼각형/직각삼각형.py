while True :
    legs = list(map(int,input().split()))
    max_l = max(legs)
    legs.sort()
    if max_l == 0 :
        break

    if legs[0]**2 + legs[1]**2 == max_l**2 :
        print('right')
    else :
        print('wrong')