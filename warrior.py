# Class for warrior
from character import Character
from dice import Die


class Warrior(Character):
    def __init__(self,isPlayer=True):
        super().__init__(isPlayer)
        self.name = "Warrior"
        self.d8 = Die(8)
        self.d4 = Die(4)
        self.maxHitPoints = self.d10.roll() + self.d10.roll() + self.d10.roll() + self.d10.roll()
        self.setInitialHitPoints()

    def attack(self) -> int:
        # unlike mugwump, warrior's attack type is passed in as a parameter.
        # roll attack die
        # determine results of attack
        if (self.isPlayer):


            print("Please select your attack type: ")
            print("1 for hit with sword")
            print("2 for hit with shield of light")
            attack_type = int(input())
            if attack_type >2 or attack_type< 0:
                print("invalid values, set to default")
                attack_type = 1
        else:
            # get attack from ai
            attack_type = self.ai()
            # roll attack die
            # determine results of attack
        damage = 0
        if attack_type <= 1:  # trusty sword
            if self.d20.roll() >= 12:  # do we hit?
                damage = self.d8.roll() + self.d8.roll()  # 2d8 for damage
                print(f"You hit with sword for {damage}")
            else:
                print("You miss!")
        else:  # (attack_type == 2): # shield of light
            if self.d20.roll() >= 6:  # do we hit
                damage = self.d4.roll()  # 1d4 damage
                print(f"You hit with shield of light for {damage}")
            else:
                print("You miss")

        # return the damage
        return damage


# testing
# x = Warrior(1)
# print (x)
# x.attack()

