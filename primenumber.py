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