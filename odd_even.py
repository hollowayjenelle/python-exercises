def odd_even():
    num = int(input("Enter a random number: "))
    if(num % 2 == 0):
        print("This number is even\n")
    else:
        print("This number is odd\n")
    
    if (num%4 == 0):
        print("This number is a multiple of 4\n")

    num1 = int(input("Enter a number you want to be dividend: "))
    check = int(input("Enter another number you want to be divisor: "))
    if (num1 % check == 0):
        print("{1} divides evenly into {0}".format(num1,check))
    else:
        print("{1} does not divide evenly into {0}".format(num1,check))  


if __name__ == '__main__':
    odd_even()
    

#The exercise comes first (with a few extras if you want the extra challenge or want to spend more time), 
# followed by a discussion. Enjoy!

#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 
# Hint: how does an even / odd number react differently when divided by 2?

#Extras:

#If the number is a multiple of 4, print out a different message.
#Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.