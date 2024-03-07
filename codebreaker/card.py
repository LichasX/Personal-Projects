inputs = str(input("")).upper().split()
cards = [x for x in range(int(inputs[0]))]
for move in inputs[2]:
    if move == "A": #card top to bottom
        cards.append(cards[0])
        del cards[0]
    elif move == "B": #card 2nd top to bottom
        cards.append(cards[1])
        del cards[1]
print(cards[int(inputs[1]) -1], cards[int(inputs[1])], cards[int(inputs[1]) + 1])
    
