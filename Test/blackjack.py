from random import shuffle

def Shf(deck):
    for q in range(4):
        shuffle(deck)

def SetCard(deck, l=[]):
    l.append(deck.pop())
    l.append(deck.pop())

def Add(deck):
    return deck.pop()

def Ace(l = [], sum = 0):

    if len(l) == 1:
        if sum + 11 <= 21:
            sum += 11
        else:
            sum += 1

def SumCard(l=[]):

    if l != ['A', 'A']:
        countAce = 0
        sum = 0
        for q in range(len(l)):
            if type(l[q]) == int:
                sum += l[q]

            elif l[q] == 'J' or l[q] == 'K' or l[q] == 'Q':
                sum += 10
            else:
                countAce += 1
                if sum + 11 <= 21:
                    sum += 11
                else:
                    sum += 1

        return sum
    else:
        return 21


if __name__ == '__main__':
    SumCard(['A'])