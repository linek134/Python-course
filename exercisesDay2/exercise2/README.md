The following changes were made to the files for the dicegame:
In the die.py:
- replaced the continue in the roll(dice) function with die(roll) to actually roll the dies.


In the runner.py:
- Fixed answer() method to correctly sum the dice values.
- Replaced while True with while c < 6 to limit the game to 6 consecutive wins.
- Added two separate variables for wins and losses to properly update the player after each round, while keeping the variable for consecutive wins (c).
- Instead of raising an error when answering "n" to the question "Would you like to play again?[Y/n]:" the game is just ended.

In the utils.py:
Declared the value in the inner function as nonlocal. 
