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
        if (self.isPlayer):
            if self.thunderCharge == 1:
                attack1 = "Tongue Whip"
                attack2 = "Gale Force Winds"
                attack3 = "Leap"
                attack4 = "Mjölnir's Power"
            if self.thunderCharge == 2:
                attack1 = "Thunder Strike"
                attack2 = "Call the Storm"
                attack3 = "Leap"
                attack4 = "Mjölnir's Power"
            if self.thunderCharge == 3:
                attack1 = "Lightning Bolt"
                attack2 = "Storm Summoning"
                attack3 = "Leap"
                attack4 = "Mjölnir's Power"
            if self.thunderCharge == 4:
                attack1 = "Hammer Throw"
                attack2 = "Weather Report"
                attack3 = "Leap"
                attack4 = "Mjölnir's Power"
            print("Please select your attack type: ")
            print(f"1 for {attack1}")
            print(f"2 for {attack2}")
            print(f"3 for {attack3}")
            print(f"4 for {attack4}")
            attack_type = int(input())
            if attack_type > 4 or attack_type < 0:
                    print(f"invalid value, set to default ({attack1})")
                    attack_type = 1
        else:
            # get attack from ai
            attack_type = self.ai()
            # roll attack die
            # determine results of attack

        damage = 0

        if attack_type == 1:  # Mjölnir attack
            if self.d20.roll() >= 4:
                damage = self.d10.roll() # 1d10
                damage = damage * self.thunderCharge # damage multiplied by thunder charge
                if self.thunderCharge == 1:
                    print("Throg can use his long tongue to attack or grab objects from a distance.")
                    print(f"{self.name} hits with {attack1} for {damage}")
                    if self.thunderCharge > 1: # Reduce Charge after successful attack
                        self.thunderCharge -= 1
                if self.thunderCharge == 2:
                    print("A powerful melee attack with the hammer that deals significant thunder damage.")
                    print(f"{self.name} hits with {attack1} for {damage}")
                    if self.thunderCharge > 1: # Reduce Charge after successful attack
                        self.thunderCharge -= 1
                if self.thunderCharge == 3:
                    print("Throg can call down a bolt of lightning to strike a single target, dealing lightning damage "
                          "and potentially stunning the target.")
                    print(f"{self.name} hits with {attack1} for {damage}")
                    if self.thunderCharge > 1: # Reduce Charge after successful attack
                        self.thunderCharge -= 1
                if self.thunderCharge == 4:
                    print(f"{self.name} spins Mjölnir channeling the power of the All-Father of Asgard")
                    print(f"{self.name} hits with {attack1} for {damage}")
                    if self.thunderCharge > 1: # Reduce Charge after successful attack
                        self.thunderCharge -= 1
            else:
                print(f"{self.name} misses with {attack1}")
                if self.thunderCharge > 1: # Reduce Charge after miss
                    self.thunderCharge -= 1

        elif attack_type == 2:  # Thunder attack
            if self.d20.roll() >= 10:
                damage = self.d10.roll() + self.d10.roll()  # 2d10
                damage = damage * self.thunderCharge  # damage multiplied by thunder charge
                if self.thunderCharge == 1:
                    print("Throg can create powerful gusts of wind to knock back enemies and objects.")
                    print(f"{self.name} hits with {attack2} for {damage}")
                    if self.thunderCharge > 1:  # Reduce Charge after successful attack
                        self.thunderCharge -= 1
                if self.thunderCharge == 2:
                    print("Throg can summon a storm in a large area, causing rain, wind, and lightning strikes. "
                          "This can provide cover, hinder enemies, and deal damage.")
                    print(f"{self.name} hits with {attack2} for {damage}")
                    if self.thunderCharge > 1:  # Reduce Charge after successful attack
                        self.thunderCharge -= 1
                if self.thunderCharge == 3:
                    print("Throg can control the weather to create a storm")
                    print(f"{self.name} hits with {attack2} for {damage}")
                    if self.thunderCharge > 1:  # Reduce Charge after successful attack
                        self.thunderCharge -= 1
                if self.thunderCharge == 4:
                    print("Throg is embued with lightning and strikes the sky, "
                          "brining forth a pouring of dart frogs from the sky.")
                    print(f"{self.name} hits with {attack2} for {damage}")
                    if self.thunderCharge > 1:  # Reduce Charge after successful attack
                        self.thunderCharge -= 1
            else:
                print(f"{self.name} misses with {attack2}")
                if self.thunderCharge > 1:  # Reduce Charge after miss
                    self.thunderCharge -= 1

        elif attack_type == 3: # Leap
            damage = 0
            if self.thunderCharge == 1:
                print("Throg leaps into the sky, but nothing happened.")
            if self.thunderCharge == 2:
                print("Throg leaps into the sky, shaking the ground beneath him, lightning strikes him,"
                      "embuing him with increased resistance to physical and magical damage")
                self.resistance = 1
                if self.thunderCharge > 1:  # Reduce Charge after successful attack
                    self.thunderCharge -= 1
            if self.thunderCharge == 3:
                print("Throg can inspire nearby allies, granting them temporary bonuses to their attacks and defenses.")
                print(f"{self.name} hits with {attack3} for {damage}")
                if self.thunderCharge > 1:  # Reduce Charge after successful attack
                    self.thunderCharge -= 1
            if self.thunderCharge == 4:
                print("Throg can inspire nearby allies, granting them temporary bonuses to their attacks and defenses.")
                damage = -1 * self.d10.roll()
                print(f"{self.name} heals for {-1 * damage}")
                if self.thunderCharge > 1:  # Reduce Charge after successful attack
                    self.thunderCharge -= 1

        else:  # All-Father Power (Charge Up)
            print(f"{self.name} spins Mjölnir channeling the power of the All-Father")
            if self.thunderCharge >= 1 and self.thunderCharge <= 4: #Ensures thunder charge between 1-4
                self.thunderCharge += 1
                if self.thunderCharge == 4: # Notifies player once thunder charge is fully charged
                    print(f"{self.name} is fully charged.")
            else: # Notifies player thunder charge is fully charge if they try to charge beyond 4, nothing will happen.
                print(f"{self.name} is fully charged.")

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

        if roll <= 3:  # 20%
            # Mjölnir attack
            attack_type = 1
        elif roll <= 6:  # 20%
            # Thunder Attack
            attack_type = 2

        elif roll <= 8:  # 80%
            # charge the suit
            attack_type = 3
        else:
            # heal
            attack_type = 4
        return attack_type