from random import randint
from datetime import datetime



def fopen(file):
    f = open(file, "r", encoding='utf-8')
    for q in f:
        print(q, end='')
    f.close()
    print('\n')

def save(pet, today):
    f = open("Save.txt", "w", encoding='utf-8')
    f.write(str(today) + '\n')
    f.write(pet.name + '\n')
    f.write(pet.kind + '\n')
    f.write(str(pet.hunger) + '\n')
    f.write(str(pet.boredom) + '\n')
    f.write(str(pet.fatigue) + '\n')
    f.write(str(pet.s) + '\n')
    f.close()

def load(pet, today):
    f = open("Save.txt", "r", encoding='utf-8')
    if f.readline() != '':
        today = f.readline()
        pet.name = f.readline().rstrip()
        pet.kind = f.readline().rstrip()
        pet.hunger = int(f.readline().rstrip())
        pet.boredom = int(f.readline().rstrip())
        pet.fatigue = int(f.readline().rstrip())
        pet.s = int(f.readline().rstrip())

    else:
        print("No saving!")
        f.close()

def today():
    return datetime.now()

def time(a, b):
    l = []
    c = b - a
    c = str(c)
    l.append(c[0])
    l.append(c[2])
    l.append(c[3])
    res = int(l[0]) * 24 + int(l[1]) * 10 + int(l[2])
    return res



class Pet():
    def __init__(self, name, kind, hunger=randint(10, 101), boredom=randint(10, 101), fatigue=randint(10, 101)):
        self.name = name
        self.kind = kind
        self.hunger = hunger
        self.boredom = boredom
        self.fatigue = fatigue
        self.s = 0

    def __str__(self):
        s = "Hunger = {0}\nBoredom = {1}\nFatigue = {2}".format(self.hunger, self.boredom, self.fatigue)
        return s

    def __down_Hunger(self):
        self.hunger -= randint(5, 21)

    def __down_Boredom(self):
        self.boredom -= randint(5, 21)

    def down_all(self):
        self.__down_Boredom()
        self.__down_Hunger()

    def happines(self):
        if (self.boredom + self.hunger + self.fatigue) >= 250:
            q = 30
        elif 200 >= (self.boredom + self.hunger + self.fatigue) < 250:
            q = (70 * 30) // 100
        elif 150 >= (self.boredom + self.hunger + self.fatigue) < 200:
            q = 15
        elif 50 >= (self.boredom + self.hunger + self.fatigue) < 100:
            q = (30 * 20) // 100

        print("Cчастье {}: ".format(self.name), "|", end='')
        for x in range(1, q):
            print("#", end='')
        q = 30 - q
        for x in range(1, q):
            print(" ", end='')
        print("|")

    def eat(self):
        self.hunger += randint(10, 25)
        self.fatigue -= 10

    def sleep(self, s):
        if s == True and self.fatigue <= 90:
            self.fatigue += randint(1, 10)
        else:
            self.fatigue -= randint(1, 10)

    def asd(self):
        self.boredom += randint(10, 25)
        self.hunger -= randint(1, 10)
        self.fatigue -= randint(1, 10)