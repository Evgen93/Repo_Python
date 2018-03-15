from random import randint
from os import system


guess = 0
guessP2 = 0
stepToWin = 0
stepToWinP2 = 0
exMode = 0
win = 0
winP2 = 0
count = 0
mode = 0
score = 10000
scoreP2 = 10000

while True:

    system("cls")

    mode = input("Выбери режим игры: 3 - с комрьютером, 2 - с другом, 1 - сам с собой, чтобы закончить игру введи Stop ")

    if mode == 'Stop' or mode == 'stop':
        break

    if int(mode) == 1:

        while exMode != 1:

            print("Введи за сколько шагов ты угадаешь число, максимум ", score / 100)
            stepToWin = input()

            while 0 > stepToWin > score / 100:

                stepToWin = input("Максимум", score / 100, "0 или меньше тоже нельзя вводить.")

            bet = score - 100 * int(stepToWin)

            while int(stepToWin) < 1 or int(stepToWin) > 10:
                stepToWin = input("Написанно же от 1 до 10! ")

            for q in range(int(stepToWin)):
                guess = input("Введи число которое выпадет на костях (1 - 12) ")

                count += 1

                while int(guess) < 1 or int(guess) > 12:
                    guess = input("Написанно же от 1 до 12! ")

                dice1 = randint(1, 6)
                dice2 = randint(1, 6)

                print(dice1 + dice2)

                if int(guess) == dice1 + dice2:
                    print("Ты угадал!")
                    win = 1
                    break
                else:
                    print("Мимо!")

                stope = input("Если хочешь закончить игрв в этом режиме напиши 'Stop', иначе нажми Enter ")

                if stope == 'stop' or stope == 'Stop':
                    break

            if win == 1:

                score += bet
                if count == 1:
                    print("Ты угадал за ", count, "шаг! ")
                    print("Очки -", score)
                    break

                elif 5 > count > 1:

                    print("Ты угадал за ", count, "шага! ")
                    print("Очки -", score)
                    break

                elif 11 > count > 5:

                    print("Ты угадал за ", count, "шагов! ")
                    print("Очки -", score)
                    break

            elif win != 1 and count == int(stepToWin):

                score -= bet
                if count == 1:

                    print("Ты не угадал за ", int(stepToWin), "шаг! ")
                    print("Очки -", score)
                    break

                elif 5 > count > 1:

                    print("Ты не угадал за ", int(stepToWin), "шага! ")
                    print("Очки -", score)
                    break
                elif 11 > count > 5:

                    print("Ты угадал за ", count, "шагов! ")
                    print("Очки -", score)
                    break

    elif int(mode) == 2:

        stepToWin = int(input("Первый игрок вводит за сколько шагов он угадает число (1 - 10) "))

        while int(stepToWin) < 1 or int(stepToWin) > 10:
            stepToWin = int(input("Написанно же от 1 до 10! "))

        stepToWinP2 = int(input("Второй игрок вводит за сколько шагов он угадает число (1 - 10) "))

        while int(stepToWinP2) < 1 or int(stepToWinP2) > 10:
            stepToWinP2 = int(input("Написанно же от 1 до 10! "))

        while (int(stepToWin) > 0 and win != 1) or (int(stepToWinP2) > 0 and winP2 != 1):

            if exMode == 1:
                break

            if int(stepToWin) > 0 and win == 0:
                guess = input("Первый игрок вводит число которое выпадет на костях (1 - 12) ")

                while int(guess) < 1 or int(guess) > 12:
                    guess = input("Написанно же от 1 до 12! ")

            if int(stepToWinP2) > 0 and winP2 == 0:
                guessP2 = input("Второй игрок вводит число которое выпадет на костях (1 - 12) ")

                while int(guessP2) < 1 or int(guessP2) > 12:
                    guessP2 = input("Написанно же от 1 до 12! ")

            dice1 = randint(1, 6)
            dice2 = randint(1, 6)

            print(dice1 + dice2)

            if int(guess) == dice1 + dice2:

                print("Первый игрок угадал! ")
                win = 1
                guess += 1

            elif stepToWin > 0:
                print("Первый игрок не угадал! ")

            if int(guessP2) == dice1 + dice2:

                print("Второй игрок угадал! ")
                winP2 = 1
                guessP2 += 1

            elif stepToWinP2 > 0:
                print("Второй игрок не угадал! ")

            stepToWin -= 1
            stepToWinP2 -= 1

            stope = input("Если хочешь закончить игрв в этом режиме напиши 'Stop', иначе нажми Enter ")

            if stope == 'stop' or stope == 'Stop':
                break

    else:

        stepToWin = int(input("Игрок вводит за сколько шагов он угадает число (1 - 10) "))

        while int(stepToWin) < 1 or int(stepToWin) > 10:
            stepToWin = int(input("Написанно же от 1 до 10! "))

        if exMode == 1:
            break

        stepToWinP2 = randint(1, 10)
        print("Комп вводит за сколько шагов он угадает число (1 - 10) ", stepToWinP2)

        while (int(stepToWin) > 0 and win != 1) or (int(stepToWinP2) > 0 and winP2 != 1):

            if int(stepToWin) > 0 and win == 0:
                guess = int(input("Игрок вводит число которое выпадет на костях (1 - 12) "))

                while int(guess) < 1 or int(guess) > 12:
                    guess = input("Написанно же от 1 до 12! ")

            if int(stepToWinP2) > 0 and winP2 == 0:

                guessP2 = randint(1, 12)
                print("Комп вводит число которое выпадет на костях (1 - 12) ", guessP2)

            dice1 = randint(1, 6)
            dice2 = randint(1, 6)

            print(dice1 + dice2)

            if int(guess) == dice1 + dice2:

                print("Игрок угадал! ")
                win = 1
                guess += 1

            elif stepToWin > 0:
                print("Игрок не угадал! ")

            if int(guessP2) == dice1 + dice2:

                print("Комп игрок угадал! ")
                winP2 = 1
                guessP2 += 1

            elif stepToWinP2 > 0:
                print("Комп не угадал! ")

            stepToWin -= 1
            stepToWinP2 -= 1

            stope = input("Если хочешь закончить игрв в этом режиме напиши 'Stop', иначе нажми Enter ")

            if stope == 'stop' or stope == 'Stop':
                break