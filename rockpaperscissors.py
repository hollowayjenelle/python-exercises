def rockpaperscissors():
    print("Welcome to the game of Rock, Paper, Scissors! Let's play!\n")
    

    ans = 'Y'

    while ans == 'Y':
        p1 = (input("Hey player one! Please enter your choice: ")).lower()
        p2 = (input("Hey player two! Please enter your choice: ")).lower()
        if (p1 == 'rock' and p2 == 'scissors'):
            print("Player one, you won the game!")
        elif (p1 == 'scissors' and p2 == 'rock'):
            print("Player two, you have won the game!")
        elif (p1 == 'scissors' and p2 == 'paper'):
            print("Player one, you have won the game!")
        elif (p1 == 'paper' and p2 == 'scissors'):
            print("Player two, you have won the game!")
        elif (p1 == 'paper' and p2 == 'rock'):
            print("Player one, you have won the game!")
        elif (p1 == 'rock' and p2 == 'paper'):
            print("Player two, you have won the game!")
        elif (p1 == p2):
            print("It's a tie!")
        else:
            print('Your choices are invalid. Please try again')
            break

        ans = (input('Do you want to play again? (Y for Yes and N for No): ')).upper()

    
if __name__ == '__main__':
    rockpaperscissors()