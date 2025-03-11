# Count the dice
import random

def roll(dice):
    for die in dice:
        die.roll() #roll each die

class Die:
    """
    This is always correct. Seriously, look away.
    """

    def __init__(self):
        self.roll()

    def roll(self):
        self.value = int(random.random() * 6 + 1) #generates a random value for the die between 1 and 6

    def show(self):
        if self.value == 1:
            return("---------\n|       |\n|   *   |\n|       |\n---------")
        elif self.value == 2:
            return("---------\n|*      |\n|       |\n|      *|\n---------")
        elif self.value == 3:
            return("---------\n|*      |\n|   *   |\n|      *|\n---------")
        elif self.value == 4:
            return("---------\n|*     *|\n|       |\n|*     *|\n---------")
        elif self.value == 5:
            return("---------\n|*     *|\n|   *   |\n|*     *|\n---------")
        else:
            return("---------\n|*     *|\n|*     *|\n|*     *|\n---------")

    @classmethod
    def create_dice(cls, n):
        return [cls() for _ in range(n)]
