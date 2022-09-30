import random

def cows(a,b):
    a = str(a)
    b = str(b)
    cow = 0
    bulls = 0
    for i in range(4):
        match = False
        for j in range(4):
            if a[i] == b[j] and i==j:
                cow += 1
                match = True
                break
        if a[i] in b and match == False:
            bulls += 1

    return (cow, bulls)

def cowsandbulls():
    print("Welcome to the game Cows and Bulls. Let's play\n")
    num = random.randint(1000,9999)
    guess = 0
    guesses = 0
    ans = 'y'
    print(num)

    while guess != num and (ans == 'y' or ans == 'yes'):
        guess = int(input("Please enter a 4 digit number: "))
        if((guess > 10000) or (guess < 1000)):
            print("Error! You have entered a 3 digit number or a 5 digit number!")
            guess = int(input("Please enter a 4 digit number: "))
        cow, bulls = cows(guess, num)
        if ((cow == 4) and (bulls == 0)):
            print("You've guessed correctly! You won the game!")
        else:
            print("{0} cow, {1} bull".format(cow, bulls))
            ans = (input("Would you like to guess again? Type Yes to continue or Exit to stop: ")).lower()
        guesses += 1
        if ans == 'exit':
            print("Aw nice try! The number was {}".format(num))
    print("It took you {} guesses".format(guesses))

if __name__ == '__main__':
    cowsandbulls()
        

#Create a program that will play the “cows and bulls” game with the user. The game works like this:

#Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. 
# For every digit that the user guessed correctly in the correct place, they have a “cow”. 
# For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
# Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.