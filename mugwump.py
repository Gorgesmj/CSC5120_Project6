from character import Character
from dice import Die


class Mugwump(Character):
    def __init__(self, isPlayer=False):
        super().__init__(isPlayer)
        self.name = "Mugwump"
        self.d100 = Die(100)
        self.d6 = Die(6)

        # The Mugwump uses six d10 to calculate their starting Hit Points
        self.maxHitPoints = (self.d10.roll() + self.d10.roll() + self.d10.roll() + self.d10.roll() + self.d10.roll()
                             + self.d10.roll())
        self.setInitialHitPoints()

    def attack(self):
        if (self.isPlayer):

            print("Please select your attack type: ")
            print("1 for hit with claws")
            print("2 for hit with fangs")
            print("3 for heal")
            attack_type = int(input())
            if attack_type >3 or attack_type< 0:
                print("invalid values, set to default")
                attack_type = 3
        else:
            # get attack from ai
            attack_type = self.ai()
            # roll attack die
            # determine results of attack


        damage = 0

        if attack_type == 1: # first attack
            if self.d20.roll() >= 13:
                damage = self.d6.roll() + self.d6.roll()
                print(f"{self.name}(Mugwump) hits with claws for {damage}")
            else:
                print(f"{self.name}(Mugwump) misses with claws")

        elif attack_type == 2:  # second attack
            if self.d20.roll() >= 16:
                damage = self.d6.roll() + self.d6.roll() + self.d6.roll()  # 3d6
                print(f"{self.name}(Mugwump) hits with fangs for {damage}")
            else:
                print(f"{self.name}(Mugwump) misses with fangs")

        else: # Heal
            damage = -1 * self.d6.roll()
            print(f"{self.name}(Mugwump) heals for {-1 * damage}")

        return damage

# # testing
# x = Mugwump(1)
# print (x)
# x.attack()
# x.setName()
# print(x.name)

