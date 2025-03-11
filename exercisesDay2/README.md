# File content for Day2 exercises
This file explains the content of the subfolders and files in exercisesDay2
## Exercise1
Subfolder exercise1 contains the folder animals, containing the created animal package with all required file.
test_animals.py contains the code to test the package
ruff_out.txt contains the output of ruff.

## Exercise2
Subfolder exercise2 contains the edited version of the buggy dice game.
The following changes have been made: 

In the die.py:
- replaced the continue in the roll(dice) function with die(roll) to actually roll the dies.


In the runner.py:
- Fixed answer() method to correctly sum the dice values.
- Replaced while True with while c < 6 to limit the game to 6 consecutive wins.
- Added two separate variables for wins and losses to properly update the player after each round, while keeping the variable for consecutive wins (c).
- Instead of raising an error when answering "n" to the question "Would you like to play again?[Y/n]:" the game is just ended.


In the utils.py:
Declared the value in the inner function as nonlocal.


## Exercise 3
Content of the files in directory exercise3
euler72.py and matmult.py are the original files
*.prof contains the output of cProfiler

matmult_modified.py: The same code as in matmult.py but written as a function.
To analyze the matmult.py with line_profiler we need an actual function
in the script to be analyzed.

profile.html and profile.json: output of Scalene

npmatmult.py: the matrix multiplication using numpy

exercises_day2_3.pdf: pdf with written exercise solutions.
