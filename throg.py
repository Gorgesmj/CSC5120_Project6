from character import Character
from dice import Die


class Throg(Character):
    def __init__(self, isPlayer=True):
        super().__init__(isPlayer)
        self.name = "Throg"
        self.d10 = Die(10)
        self.d42 = Die(42)
        self.maxHitPoints = self.d42.roll() + self.d42.roll() + self.d42.roll() + self.d42.roll()
        self.setInitialHitPoints()
        self.thunderCharge = 1
        self.resistance = 0

    def attack(self):
        if self.isPlayer:
            if self.thunderCharge == 1:
                attack1 = "Tongue Whip"
                attack2 = "Gale Force Winds"
                attack3 = "Leap"
                attack4 = "Mjölnir Spin"
            elif self.thunderCharge == 2:
                attack1 = "Thunder Strike"
                attack2 = "Call the Storm"
                attack3 = "Leap"
                attack4 = "Mjölnir Spin"
            elif self.thunderCharge == 3:
                attack1 = "Lightning Bolt"
                attack2 = "Storm Summoning"
                attack3 = "Leap"
                attack4 = "Mjölnir Spin"
            elif self.thunderCharge == 4:
                attack1 = "Hammer Throw"
                attack2 = "Weather Report"
                attack3 = "Leap"
                attack4 = "Mjölnir Spin"
            print("Please select your attack type: ")
            print(f"1 for {attack1}")
            print(f"2 for {attack2}")
            print(f"3 for {attack3}")
            print(f"4 for {attack4}")
            attack_type = int(input())
            if attack_type > 4 or attack_type < 1:
                print(f"Invalid value, set to default ({attack1})")
                attack_type = 1
        else:
            # get attack from AI
            attack_type = self.ai()

        damage = 0

        if attack_type == 1:  # Mjölnir attack
            if self.d20.roll() >= 4:
                damage = self.d10.roll()  # 1d10
                damage = damage * self.thunderCharge  # damage multiplied by thunder charge
                if self.thunderCharge == 1:
                    print(f"{self.name} (Throg) lashes out with his long tongue, dealing {damage} damage!")
                elif self.thunderCharge == 2:
                    print(f"{self.name} (Throg) strikes with a powerful melee attack, dealing {damage} thunder damage!")
                elif self.thunderCharge == 3:
                    print(f"{self.name} (Throg) calls down a bolt of lightning, stunning the enemy and dealing {damage} damage!")
                elif self.thunderCharge == 4:
                    print(f"{self.name} (Throg) spins Mjölnir, channeling the power of Asgard to deal {damage} damage!")
                self.thunderCharge = max(self.thunderCharge - 1, 1)
            else:
                print(f"{self.name} misses with {attack1}")

        elif attack_type == 2:  # Thunder attack
            if self.d20.roll() >= 10:
                damage = self.d10.roll() + self.d10.roll()  # 2d10
                damage = damage * self.thunderCharge  # damage multiplied by thunder charge
                if self.thunderCharge == 1:
                    print(f"{self.name} (Throg) creates powerful gusts of wind, dealing {damage} damage!")
                elif self.thunderCharge == 2:
                    print(f"{self.name} (Throg) summons a storm, causing chaos and dealing {damage} damage!")
                elif self.thunderCharge == 3:
                    print(f"{self.name} (Throg) controls the weather to create a storm, dealing {damage} damage!")
                elif self.thunderCharge == 4:
                    print(f"{self.name} (Throg) summons a deluge of dart frogs from the sky, dealing {damage} damage!")
                self.thunderCharge = max(self.thunderCharge - 1, 1)
            else:
                print(f"{self.name} misses with {attack2}")

        elif attack_type == 3:  # Leap
            damage = 0
            if self.thunderCharge == 1:
                print(f"{self.name} (Throg) leaps into the sky, but nothing happens.")
            elif self.thunderCharge == 2:
                print(f"{self.name} (Throg) leaps, shaking the ground and increasing his resistance to damage.")
                self.resistance = 1
            elif self.thunderCharge == 3:
                print(f"{self.name} (Throg) leaps, rallying a stampede of frogs to trample the enemy!")
            elif self.thunderCharge == 4:
                print(f"{self.name} (Throg) leaps and heals himself for {-1 * damage} HP!")
                damage = -1 * self.d10.roll()
            self.thunderCharge = max(self.thunderCharge - 1, 1)

        else:  # Mjölnir Spin (Charge Up)
            print(f"{self.name} (Throg) spins Mjölnir, channeling the power of the All-Father")
            if self.thunderCharge < 4:
                self.thunderCharge += 1
                if self.thunderCharge == 4:
                    print(f"{self.name} (Throg) is fully charged.")
            else:
                print(f"{self.name} (Throg) is already fully charged.")

        return damage

    def takeDamage(self, damage: int):
        final_damage = damage
        if self.resistance == 1:
            final_damage = final_damage // 2
            self.resistance = 0
        super().takeDamage(final_damage)

    def ai(self) -> int:  # private function to get the attack type
        attack_type = 0
        roll = self.d10.roll()

        if roll <= 3:  # 30%
            attack_type = 1
        elif roll <= 6:  # 30%
            attack_type = 2
        elif roll <= 8:  # 20%
            attack_type = 3
        else:  # 20%
            attack_type = 4
        return attack_type


# Test code should only run when this script is executed directly
if __name__ == "__main__":
    x = Throg(True)
    print(f"Begin HP: {x.hitPoints}")
    x.attack()
    x.takeDamage(10)
    print(x.hitPoints)
    damage = x.attack()
    print(x.hitPoints)
    print(x.outputData())
    print(x.loadData("Genius", 15, 20))
    print(x.outputData())