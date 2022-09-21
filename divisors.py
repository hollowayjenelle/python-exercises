def divisors():
    num = int(input("Enter a number you'd like to find the divisors for within that range: "))
    lst2 = range(1,num+1)
    divisorlst2 = [y for y in lst2 if num%y == 0]
    print(divisorlst2)

if __name__ == '__main__':
    divisors()


#Create a program that asks the user for a number and then 
# prints out a list of all the divisors of that number. 
# (If you don’t know what a divisor is, it is a number that divides evenly into another number. 
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)