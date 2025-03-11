from .die import Die
from .utils import i_just_throw_an_exception

class GameRunner:

    def __init__(self):
        self.dice = Die.create_dice(5)
        self.reset()

    def reset(self):
        self.round = 1
        self.wins = 0
        self.loses = 0

    def answer(self):
        total = 0
        for die in self.dice:
            total += die.value #add actual values of each die
        return total

    @classmethod
    def run(cls):
        total_wins = 0  # Track total wins across all rounds
        total_losses = 0  # Track total losses across all rounds
        c = 0 #variable counting consecutive wins
        while c < 6: #allow max 6 consecutive wins
            runner = cls()

            print("Round {}\n".format(runner.round))

            for die in runner.dice:
                print(die.show())

            guess = input("Sigh. What is your guess?: ")
            guess = int(guess)

            if guess == runner.answer():
                print("Congrats, you can add like a 5 year old...")
                runner.wins += 1
                total_wins += 1  # Increment total wins
                c += 1
            else:
                print("Sorry that's wrong")
                print("The answer is: {}".format(runner.answer()))
                print("Like seriously, how could you mess that up")
                runner.loses += 1
                total_losses += 1  # Increment total losses
                c = 0
            print("Total Wins: {} Total Losses: {}".format(total_wins, total_losses))
            runner.round += 1

            if c == 6:
                print("You won... Congrats...")
                print("The fact it took you so long is pretty sad")
                break

            prompt = input("Would you like to play again?[Y/n]: ")

            if prompt == 'y' or prompt == '':
                continue
            elif prompt == 'n' or prompt == 'N':
                break
            else:
                i_just_throw_an_exception()
		
