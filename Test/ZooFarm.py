import os, random

class Food():
    def __init__(self, name, satur, price):
        self.name = name
        self.satur = satur
        self.price = price

banana = Food("Banana", 10, 5)
apple = Food("Apple", 5, 2)
meat = Food("Meat", 30, 15)
bone = Food("Bone", 15, 7)
fish = Food("Fish", 15, 8)
milk = Food("Milk", 14, 6)

class Critter():
    def __init__(self, name, hunger=random.randint(10, 101), boredom=random.randint(10, 101), fatigue=random.randint(10, 101)):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        self.fatigue = fatigue

    def __str__(self):
        print("Hunger =", self.hunger, "\nBoredom =", self.boredom, "\nFatigue =", self.fatigue)
        return ""

    def eat(self, obj):
        self.hunger += obj.satur
        self.fatigue -= 10

    def mood(self):
        mod = self.hunger + self.boredom + self.fatigue
        if 250 < mod <= 300 or mod > 300:
            res = "I am vary happy!"
            return res
        elif 200 < mod <= 250:
            res = "I am normal"
            return res



    def talk(self):
        print('I am', self.name, 'and', self.mood())



def main():
    name = input("What name of your pet? \n")
    pet = Critter(name)

    while True:
        print("""
        0 - exit game;
        1 - talk with {};
        2 - eat to {};
        3 - play to {};
        """.format(name, name, name))

        choice = input("choice game mode: \n")
        if choice == '0':
            exit()
        elif choice == '1':
            pet.talk()
        elif choice == '2':
            pet.eat(meat)
        elif choice == '3':
            pet.play()
        elif choice == 'show':
            print(pet)
        else:
            print("Wrong choice")

        os.system("cls")

if __name__ == '__main__':
    main()