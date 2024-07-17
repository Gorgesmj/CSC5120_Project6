from character import Character
from dice import Die


class spooderman(Character):
    def __init__(self, isPlayer=True):
        super().__init__(isPlayer)
        self.name = "spooderman"
        self.d10 = Die(10)
        self.d100 = Die(100)
        self.maxHitPoints = self.d100.roll() + self.d100.roll() + self.d100.roll()
        self.setInitialHitPoints()
        self.spooderSense = 0

    def attack(self):
        if (self.isPlayer):

            print("Please select your attack type: ")
            print("1 for roast")
            print("2 for web blast")
            print("3 for spooder sense charge up (triple damage next attack)")
            print("4 for steal lunch money (heal)")
            attack_type = int(input())
            if attack_type > 4 or attack_type < 0:
                print("invalid values, steal lunch money")
                attack_type = 4
        else:
            # get attack from ai
            attack_type = self.ai()
            # roll attack die
            # determine results of attack

        damage = 0

        if attack_type == 1:  # first attack
            if self.d20.roll() >= 5:
                damage = self.d10.roll() + self.d10.roll()
                if self.spooderSense == 1:
                    damage = damage * 3
                    self.spooderSense = 0
                print(f"{self.name} spooderman delivers a tasteful roast for {damage}")
            else:
                print(f"{self.name} spooderman said something out of pocket")

        elif attack_type == 2:  # second attack
            if self.d20.roll() >= 10:
                damage = self.d10.roll() + self.d10.roll() + self.d10.roll()  # 3d10
                if self.spooderSense == 1:
                    damage = damage * 3
                    self.spooderSense = 0
                print(f"{self.name} (spooderman) delivers a web blast for {damage}")
            else:
                print(f"{self.name} (spooderman) web blast misses ")
        elif attack_type == 3:
            self.spooderSense = 1
            print(f"{self.name} (spooderman) spooder sense charged!")
            damage = 0

        else:  # Heal
            damage = -1 * self.d6.roll()
            print(f"{self.name}(spooderman) steal lunch money and heals for {-1 * damage}")

        return damage

    def takeDamage(self, damage: int):
        final_damage = damage
        if self.spooderSense == 1 and damage > 0:
            final_damage = final_damage // 2

        super().takeDamage(final_damage)


# test
if __name__ == "__main__":
    x = spooderman(True)
    print(f"Begin HP: {x.hitPoints}")
    x.attack()
    x.takeDamage(10)
    print(x.hitPoints)
    #
    damage = x.attack()
    print(x.hitPoints)
    print(x.outputData())
    print(x.loadData("Genius",15,20))
    print(x.outputData())