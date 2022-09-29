def reverseword():
    sentence = input("Please enter a random sentence: ")
    str1 = sentence.split()
    str1.reverse()
    result = " ".join(str1)
    print(result)

if __name__ == '__main__':
    reverseword()