import blackjack

p1 = []
dealer = []
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4

print("Welcome to the Blackjack!")

blackjack.Shf(deck)

blackjack.SetCard(deck, p1)
blackjack.SetCard(deck, dealer)

sumD = blackjack.SumCard(dealer)

while sumD < 17:
    dealer.append(blackjack.Add(deck))
    sumD = blackjack.SumCard(dealer)

sumP1 = blackjack.SumCard(p1)

print("Yor deck :", p1)
print("Yor score :", sumP1)

while sumP1 != 21:

    a = input("Another card? (Y/N)")
    if a == 'Y' or a == 'y':
            p1.append(blackjack.Add(deck))
            sumP1 = blackjack.SumCard(p1)
            print("Yor deck :", p1)
            print("Yor score :", sumP1)
            if sumP1 > 21:
                break
    else:
        break

print("Dealer deck :", dealer)
print("Dealer score :", sumD)

if 21 >= sumD > sumP1:
    print("Dealer Win!")
elif 21 >= sumP1 > sumD:
    print("You Win!")
elif sumD < sumP1:
    print("Dealer Win!")
elif sumD > sumP1:
    print("You Win!")
else:
    print("Draw!")