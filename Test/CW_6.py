from random import randint

step = 0
frStep = 0
guess = 0
friendGuess = 0
mode = 0
frScore = 1000
score = 1000
bet = 1000
frBet = 1000
endP = 0
endF = 0
ex = 0

while True:

    print("Выбери режим игры: 1 - с комрьютером, 2 - с другом, 3 - сам с собой")
    mode = int(input("Введи номер режима"))

    if mode < 1 or mode > 3:
        mode = 3

    if mode == 3:

        print("За какое количество попыток ты угадаешь число?\nВведи число от 1 до 10")
        print("максимум 10 попыток, 1 попытка 100 очков")
        step = int(input())
        bet /= step
        while (step < 1 or step > 10) or bet > score:
            if step < 1 or step > 10:
                step = int(input("от 1 до 10"))
            if bet > score:
                print("У тебя не хватает очков для ставки, максимум шагов ", int(score / 100))
                step = int(input())

        while step > 0:

            guess = int(input("Выбери число от 1 до 12"))
            while guess < 1 or guess > 12:
                guess = int(input("написано же от 1 до 12...\nДавай еще разок"))

            dice1 = randint(1, 6)
            dice2 = randint(1, 6)

            print(dice1 + dice2)

            if guess == dice1 + dice2:
                print("Угадал!")
                guess = 0
                break
            else:
                print("Мимо.")

            step -= 1

        if guess == 0:
            print("Красава, ты выиграл ", bet, " очков")
            score += bet
            print(score)
        else:
            print("Ты проиграл ", bet, " очков")
            score -= bet
            print(score)

    elif mode == 2:

        print("Первый игрок вводи количество попыток\nВведи число от 1 до 10")
        print("максимум 10 попыток, 1 попытка 100 очков")
        step = int(input())
        bet /= step

        while (step < 1 or step > 10) or bet > score:
            if step < 1 or step > 10:
                step = int(input("от 1 до 10"))
            if bet > score:
                print("У тебя не хватает очков для ставки, максимум шагов ", int(score / 100))
                step = int(input())

        print("Второй игрок вводи количество попыток\nВведи число от 1 до 10")
        print("максимум 10 попыток, 1 попытка 100 очков")
        frStep = int(input())
        frBet /= frStep

        while (step < 1 or frStep > 10) or frBet > frScore:
            if step < 1 or frStep > 10:
                frStep = int(input("от 1 до 10"))
            if bet > frScore:
                print("У тебя не хватает очков для ставки, максимум шагов ", int(frScore / 100))
                frStep = int(input())

        while step > 0 and frStep > 0:

            guess = int(input("Первый игрок загадывает число от 1 до 12"))
            while guess < 1 or guess > 12:
                guess = int(input("написано же от 1 до 12...\nДавай еще разок"))

            print("Второй игрок загадывает число от 1 до 12 кроме ", guess)
            friendGuess = int(input())
            while (friendGuess < 1 or guess > 12) or friendGuess == guess:
                if friendGuess < 1 or guess > 12:
                    friendGuess = int(input("написано же от 1 до 12...\nДавай еще разок"))
                elif friendGuess == guess:
                    print(guess, " выбрал первый игрок...\nДавай еще разок")
                    friendGuess = int(input())

            dice1 = randint(1, 6)
            dice2 = randint(1, 6)

            print(dice1 + dice2)

            if guess == dice1 + dice2:
                print("Первый игрок выиграл!")
                endP = 1
                score += bet
                frScore -= frBet
                print(score)
                print(frScore)

            elif friendGuess == dice1 + dice2:
                print("Второй игрок выиграл!")
                endF = 1
                score -= bet
                frScore += frBet
                print(score)
                print(frScore)

            else:
                print("Оба игрока лузеры")
                score -= bet
                frScore -= frBet
                print(score)
                print(frScore)
            step -= 1
            frStep -= 1

    else:
        guess = int(input("Игрок загадывает число от 1 до 12"))
        while guess < 1 or guess > 12:
            gues = int(input("написано же от 1 до 12...\nДавай еще разок"))

        print("Комп загадывает число")
        friendGuess = (randint(1, 6) + randint(1, 6))
        print(friendGuess)

        dice1 = randint(1, 6)
        dice2 = randint(1, 6)

        print(dice1 + dice2)

        if guess == dice1 + dice2:
            print("Игрок выиграл!")

        elif friendGuess == dice1 + dice2:
            print("Комп выиграл!")

        else:
            print("Оба лузеры")

