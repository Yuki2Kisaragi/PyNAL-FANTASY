import sys


class hero():
    def __init__(self, hp, power):
        self.life = hp
        self.attack = power

    def battle(self, hp, damage):
        self.life = hp - damage
        if self.life <= 0:
            print("Hero is Down !")
            print("Darkness came to the World...")
            sys.exit()
        else:
            print("Hero HP:", self.life)
            return self.life


class satan():
    def __init__(self, hp, power):
        self.life = hp
        self.attack = power

    def battle(self, hp, damage):
        self.life = hp - damage
        if self.life <= 0:
            print("Satan is Down !")
            print("The World is Saved !!")
            sys.exit()
        else:
            print("Satan HP:", self.life)
            return self.life


hero = hero(60, 25)
satan = satan(100, 15)

# print(hero.life)
# print(hero.attack)
#
# print(satan.life)
# print(satan.attack)

print("Battle Start!")
i = 1
while True:
    print("Turn:", i)
    print("Hero's attack!"+ str(satan.attack) + " Damage!")
    satan.battle(satan.life, hero.attack)
    print("Sattan's attack! " + str(satan.attack) + " Damage!")
    hero.life = hero.battle(hero.life, satan.attack)
    i += 1
