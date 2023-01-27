while True :
    in_n = input()
    if in_n == '0' :
        break
    rev_n = in_n[::-1]
    if in_n == rev_n :
        print('yes')
    else :
        print('no')