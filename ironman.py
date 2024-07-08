from character import Character
from dice import Die


class IronMan(Character):
    def __init__(self, isPlayer=True):
        super().__init__(isPlayer)
        self.name = "IronMan"
        self.d10 = Die(10)
        self.d42 = Die(42)
        self.maxHitPoints = self.d42.roll() + self.d42.roll() + self.d42.roll() + self.d42.roll()
        self.setInitialHitPoints()
        self.suitCharged = 0

    def attack(self):
        if (self.isPlayer):

            print("Please select your attack type: ")
            print("1 for hit with hand blaster")
            print("2 for hit with laser")
            print("3 for charge the suit(next time must hit and double damage)")
            print("4 for fix the armor ")
            attack_type = int(input())
            if attack_type > 4 or attack_type < 0:
                print("invalid values, set to default(charge the suit)")
                attack_type = 3
        else:
            # get attack from ai
            attack_type = self.ai()
            # roll attack die
            # determine results of attack

        damage = 0

        if attack_type == 1:  # first attack
            if self.d20.roll() >= 5:
                damage = self.d10.roll() + self.d10.roll()
                if self.suitCharged == 1:
                    damage = damage * 2
                    self.suitCharged = 0
                print(f"{self.name}(IronMan) hits with hand blaster for {damage}")
            else:
                print(f"{self.name}(IronMan) misses with hand blaster")

        elif attack_type == 2:  # second attack
            if self.d20.roll() >= 10:
                damage = self.d10.roll() + self.d10.roll() + self.d10.roll()  # 3d10
                if self.suitCharged == 1:
                    damage = damage * 2
                    self.suitCharged = 0
                print(f"{self.name}(IronMan) hits with laser for {damage}")
            else:
                print(f"{self.name}(IronMan) misses with laser")
        elif attack_type == 3:
            self.suitCharged = 1
            print(f"{self.name}(IronMan) suit charged")
            damage = 0

        else:  # Heal
            damage = -1 * self.d6.roll()
            print(f"{self.name}(IronMan) heals for {-1 * damage}")

        return damage

    def takeDamage(self, damage: int):
        final_damage = damage
        if self.suitCharged == 1:
            final_damage = final_damage // 2

        super().takeDamage(final_damage)


# test
x = IronMan(True)
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