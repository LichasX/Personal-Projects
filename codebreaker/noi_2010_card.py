#https://codebreaker.xyz/problem/card, tle 1s from 1s
inputs = str(input()).split()
cards = [x for x in range(int(inputs[0]))]
for move in inputs[2]:
    if move == "A": #card top to bottom
        cards.append(cards.pop(0))
    elif move == "B": #card 2nd top to bottom
        cards.append(cards.pop(1))
print(cards[int(inputs[1]) -1], cards[int(inputs[1])], cards[int(inputs[1]) + 1])
