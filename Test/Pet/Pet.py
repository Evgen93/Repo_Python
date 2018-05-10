import Pet_lib, os

img_dict = {"Собака": "dog.txt", "Курица": "chik.txt", "Корова": "cow.txt", "Свинья": "pig.txt", "Кот": "cat.txt", "Дракон": "dragon.txt"}
pet_dict = {'1': "Собака", '2': "Курица", '3': "Корова", '4': "Свинья", '5': "Кот", '6': "Дракон"}
l = [str(x) for x in range(1, 7)]
today = ''
print("Добро пожаловать в игру Pet!")

exit = 1
while exit == 1:
    choice = input("""
1 - Новая игра;
2 - Продолжить;
0 - Выход из игры;
""")
    os.system("cls")
    if choice == '0':
        exit()

    elif choice == '1':
        today = Pet_lib.today()
        end = 1
        while end == 1:
            print("Выберите питомца:")
            count = 1
            for q in pet_dict.values():
                print("{} - {}".format(count, q), "\b;")
                count += 1

            choice = input()
            for q in l:
                if choice == q:
                    _pet = choice
                    end = 0
                    break
            if end == 1:
                print("Введено неверное значение:")
                input()
            os.system("cls")

        name = input("Введите имя питомца:")
        pet = Pet_lib.Pet(name, pet_dict[_pet])
        exit = 0
    elif choice == '2':
        pet = Pet_lib.Pet("chappie", "собака")
        Pet_lib.load(pet, today)
        exit = 0

while True:
    if pet.s == 0:
        os.system("cls")
        Pet_lib.fopen(r"img\{}".format(img_dict[pet.kind]))

        Pet_lib.fopen(r"Menu.txt")

        choice = input()
        if choice == '5':
            break
        elif choice == "show":
            os.system("cls")
            print(pet)
            input()

        elif choice == '1':
            os.system("cls")
            pet.happines()
            os.system("pause")

        elif choice == '2':
            os.system("cls")
            if pet.hunger <= 80:
                print("Ом-ном-ном-ном...")
                pet.eat()
            else:
                print("{} сыт".format(pet.name))
            os.system("pause")

        elif choice == '3':
            os.system("cls")
            print("Вы играете с {}".format(pet.name))

            if pet.boredom <= 90:
                pet.asd()

            os.system("pause")

        elif choice == '4':
            sleep = 1
            print("ZzZzZzZzZzZzZz...")
            pet.s = 1
            os.system("pause")

        Pet_lib.save(pet, today)
    else:
        os.system("cls")
        Pet_lib.save(pet, today)
        print("{} cпит".format(pet.name))
        choice = input("разбудить - 1\nвыход - 0\n")
        if choice == '1':
            pet.s = 0
            os.system("cls")
        elif choice == '0':
            exit = 0
            break
