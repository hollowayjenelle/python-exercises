def palindrome():
    s = (input("Enter a word:\t")).lower()
    if s == s[::-1]:
        print('{} is a palindrome'.format(s))
        #a palindrome is a string that reads
        #the same forwards and backwards
    else:
        print('{} is not a palindrome'.format(s))

if __name__ == '__main__':
    palindrome()