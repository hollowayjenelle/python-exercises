def divisors():
    x = int(input("Enter a number where you'd like to start your range: "))
    y = int(input("Enter another number where you'd like to end your range: "))
    lst = range(x,y+1)

    num = int(input("Enter a number you'd like to find the divisors for within that range: "))
    divisorlst = [x for x in lst if num%x == 0]
    print(divisorlst)

if __name__ == '__main__':
    divisors()


#Create a program that asks the user for a number and then 
# prints out a list of all the divisors of that number. 
# (If you don’t know what a divisor is, it is a number that divides evenly into another number. 
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)