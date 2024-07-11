from character import Character
from dice import Die


class MichaelNewChar(Character):
    def __init__(self, isPlayer=True):
        super().__init__(isPlayer)
        self.name = "TBD"
        self.d10 = Die(10)
        self.d20 = Die(20)
        self.maxHitPoints = self.d20.roll()
        self.setInitialHitPoints()
