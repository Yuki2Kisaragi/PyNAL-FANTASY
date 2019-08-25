
import sys

class Person():
    def __init__(self, Char_name, Max_HP, Power):
        self.life = 0
        self.name = Char_name
        self.Max_life = Max_HP
        self.attack = Power

    def char_status(self, HP):
        print("{} HP:{}/{}".format(self.name, HP, self.Max_life))
        [print("|", end='') for i in range(50)]
        print('\n')

    def battle(self, HP, Damage):
        self.life = HP - Damage
        self.char_status(self.life)

        if self.life <= 0:
            print(self.name + " is Down !")
            # print("Darkness came to the World...")
            sys.exit()
        else:
            print(self.name + " HP:{}".format(self.life))
            return self.life


Hero = Person("Hero", 150, 40)
Satan = Person("Satan", 250, 20)

# class hero(person):
# def __init__(self, hp, power):
#     self.life = hp
#     self.attack = power

# def battle(self, hp, damage):
#     self.life = hp - damage
#     if self.life <= 0:
#         print("Hero is Down !")
#         print("Darkness came to the World...")
#         sys.exit()
#     else:
#         print("Hero HP:", self.life)
#         return self.life


# class satan():
#     def __init__(self, hp, power):
#         self.life = hp
#         self.attack = power
#
#     def battle(self, hp, damage):
#         self.life = hp - damage
#         if self.life <= 0:
#             print("Satan is Down !")
#             print("The World is Saved !!")
#             sys.exit()
#         else:
#             print("Satan HP:", self.life)
#             return self.life


print("Battle Start!")
Hero.char_status(Hero.Max_life)
Satan.char_status(Satan.Max_life)

i = 1
while True:
    print("Turn:", i)
    print("Hero's attack!" + str(Satan.attack) + " Damage!")
    Satan.battle(Satan.life, Hero.attack)
    print("Sattan's attack! " + str(Satan.attack) + " Damage!")
    Hero.life = Hero.battle(Hero.life, Satan.attack)
    i += 1
