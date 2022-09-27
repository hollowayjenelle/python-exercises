def divisors(num):
    lst = range(1,num+1)
    divisorlst = [y for y in lst if num%y == 0]
    return (divisorlst)

def primenumber():
    num1 = int(input("Please enter a number: "))
    lst = divisors(num1)
    if (len(lst) <= 2):
        print("The number {} is a prime number".format(num1))
    else:
        print("The number {} is not a prime number".format(num1))

if __name__ == '__main__':
    primenumber()

#Ask the user for a number and determine whether the number is prime or not.
#  (For those who have forgotten, a prime number is a number that can be divided by itself and 1.). 
# You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, 
# described below.