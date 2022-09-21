def lessthanten():
    a = [1,1,2,3,5,6,13,21,34,55,89]
    num = int(input('Please enter a number: '))
    newlst = [x for x in a if x < num]
    print (newlst)

if __name__ == '__main__':
    lessthanten()