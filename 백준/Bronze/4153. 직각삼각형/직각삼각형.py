while True :
    legs = list(map(int,input().split()))
    legs.sort()
    if legs[-1] == 0 :
        break

    if legs[0]**2 + legs[1]**2 == legs[2]**2 :
        print('right')
    else :
        print('wrong')