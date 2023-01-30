N = int(input())

deck = list(range(1,N+1))

isfirst = True
last_card = deck[-1]
history = [last_card]
while len(deck) > 1 :
    if not isfirst :
        last_card = history[-2]

    if last_card == deck[-1] :
        iseven = True
    else :
        iseven = False

    if isfirst or iseven:
        deck = deck[1::2]
        isfirst = False
    else :
        deck = deck[0::2]
    history.append(deck[-1])
    if len(deck) == 1 :
        break
        
print(deck[0])
