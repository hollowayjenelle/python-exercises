def removeduplicates(a):
    return list(set(a))

def removeduplicates2(a):
    newlst = []
    for x in a:
        if x not in newlst:
            newlst.append(x)
    return newlst

if __name__ == '__main__':
    a = [1,1,5,7,8,9,9,9,10,12,12]
    print(removeduplicates(a))
    print(removeduplicates2(a))