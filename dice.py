# Dice Class notes:
# NumSides
# Current Value
# Random Num Generator
import random


# Functions
# Die(numSides)
# getCurrentValue: int
# roll : None
# Dice Class

##__ means a private

class Die:
    def __init__(self, numSides=6, seed=None):
        random.seed(seed)
        if numSides > 100 or numSides < 1:
            numSides = 6

        self.sides = numSides
        self.currentValue = self.roll()



    def get_current_value(self) -> int:
        return self.currentValue
        # return the current value

    def roll(self):
        # roll the die
        return random.randint(1, self.sides)

# # Testing Codes
# x = Die(10)
# x.roll()
# print(x.get_current_value())
