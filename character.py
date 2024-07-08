from dice import Die


# Parental Class for Mugwump and Warrier

class Character:
    def __init__(self, isPlayer: bool):
        self.d20 = Die(20)
        self.d10 = Die(10)
        self.maxHitPoints = None
        self.hitPoints = None
        self.name = None
        self.isPlayer = isPlayer

    def setInitialHitPoints(self):
        self.hitPoints = self.maxHitPoints

    def getHitPoints(self):
        return self.hitPoints

    def takeDamage(self, damage: int):
        if self.hitPoints >= damage:
            self.hitPoints -= damage
            # if we actually just healed, we should make sure we don't exceed max Hitpoints
            if self.hitPoints > self.maxHitPoints:
                self.hitPoints = self.maxHitPoints
        else:
            self.hitPoints = 0

    def attack(self):
        pass

    def __repr__(self):
        result = f" {self.name} HP : {self.hitPoints}"
        return result

    def ai(self) -> int:  # private function to get the attack type
        attack_type = 0
        roll = self.d20.roll()

        if roll <= 12:  # 60%
            # Razor - Sharp Claws
            attack_type = 1
        elif roll <= 17:  # 25%
            # Their Fangs of Death
            attack_type = 2
        else:
            # heal 15%
            attack_type = 3
        return attack_type