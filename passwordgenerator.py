import string
import random
def pwgenerator(num):
    pw = string.ascii_letters + string.digits + string.punctuation
    #result = "".join(random.sample(pw,num))
    result = "".join(random.choice(pw) for _ in range(num))
    #both versions work
    return result

if __name__ == '__main__':
    ans = input("Would you like to generate a password? Y for yes, N for no: ")
    while ans == 'y' or ans == 'Y':
        num = int(input("How long do you want your password to be: "))
        password = pwgenerator(num)
        print("Your password is {}".format(password))
        ans = input("Would you like to generate another password? Y for yes, N for no: ")
    
    
        

#Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
# The passwords should be random, generating a new password every time the user asks for a new password. 
# Include your run-time code in a main method