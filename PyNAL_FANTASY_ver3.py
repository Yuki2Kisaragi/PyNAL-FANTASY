import sys


# sys.exit()を使用する

class Person():
    def __init__(self, char_name, max_hp, power):
        self.life = max_hp
        self.name = char_name
        self.Max_life = max_hp
        self.attack = power

    def char_status(self, hp):
        HP_Percentage = round(hp / self.Max_life, 1)
        bar = int(50 * HP_Percentage)
        print("{} HP:{}/{}".format(self.name, hp, self.Max_life))
        [print("|", end='') for i in range(bar)]
        print('\n')

        if self.life <= 0:
            print(self.name + " is Down !")
            # print("Darkness came to the World...")
            sys.exit()

    def battle(self, hp, damage):
        self.life = hp - damage
        # self.char_status(self.life)


Hero = Person("Hero", 150, 40)
Satan = Person("Satan", 250, 20)

Hero.char_status(Hero.Max_life)
Satan.char_status(Satan.Max_life)

print("Battle Start!")

i = 1
while True:
    print("Turn:{}".format(i))
    print("Hero's attack! " + str(Hero.attack) + " Damage!")
    Satan.battle(Satan.life, Hero.attack)
    print("Satan's attack! " + str(Satan.attack) + " Damage!")
    Hero.battle(Hero.life, Satan.attack)
    Hero.char_status(Hero.life)
    Satan.char_status(Satan.life)
    i += 1
    input()
    # 自動スクロールを止める