import random
import sys

def guessinggame():
    num = random.randint(1,9)
    guesses = 0
    ans = 'yes'

    while (ans == 'yes' or ans == 'y'):
        user_guess = int(input("Guess a number between 1 and 9 (including 1 and 9): "))
        if (user_guess < num):
            guesses += 1
            print("You've guessed too low. Try again")

        elif (user_guess > num):
            guesses += 1
            print("You have guessed too high! Try again!")
        else:
            (user_guess == num)
            guesses += 1
            print("You have guessed correctly! Congrats")
            break

        ans = (input("Do you want to try again? Yes or Exit: ")).lower()
    
    print("You have guessed this many times: {}".format(guesses))


if __name__ == '__main__':
    guessinggame()

        
