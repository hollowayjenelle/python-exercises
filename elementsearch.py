def elementsearch(arr, num):
    if num in arr:
        return True
    else:
        return False

def binarysearch(arr, low, high, num):
    if high >= low:
        mid = int((high + low) // 2)
        if arr[mid] == num:
            return True   
        elif arr[mid] > num:
            return binarysearch(arr, low, mid-1, num)
        else: 
            return binarysearch(arr, mid+1, high, num)
    else:
        return False
    
if __name__ == '__main__':
    a = [1,3,5,30,42,43,500]
    user_num = int(input("Please enter a number you'd like to search for in the list (True it is in the list, False it isnt): "))
    print(elementsearch(a,user_num))
    print(binarysearch(a, 0, len(a)-1, user_num))
    