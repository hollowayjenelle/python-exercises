def character_input():
    name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))
    currentYear = 2022
    one_hun = 2022 + (100-age)
    print("Your name is {0} and you will be 100 in the year {1}".format(name, one_hun))
    num = int(input("How many times would you like for the above message to be printed out: "))
    print(num * "Your name is {0} and you will be 100 in the year {1}\n".format(name, one_hun))

if __name__ == '__main__':
    character_input()