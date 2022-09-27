import random

def listoverlap2():
    a = random.sample(range(100), 6)
    b = random.sample(range(100), 6)

    newlst = [x for x in a if x in b]
    print(newlst)

if __name__ == '__main__':
    listoverlap2()