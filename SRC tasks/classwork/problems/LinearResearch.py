array = [1,2,3,4,5,6,7,8]
def linearsearch(arr,item):
    index = -1
    i = 0
    found  = False
    while found == False and len(arr) != i + 1:
        if arr[i] == item:
            found = True
            index = i
        i +=1
        # end if
    # end while
    return index

print(linearsearch(array,5))