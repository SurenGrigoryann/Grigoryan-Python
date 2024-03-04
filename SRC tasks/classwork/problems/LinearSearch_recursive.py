array = [1,2,3,4,5,6,7,8]
def linearsearch_recursive(arr,item,index):
    index = index + 1
    if index == len(arr):
        return False
    if arr[0] == item:
        return index
    else:
        return linearsearch_recursive(arr[1:],item,index)

print(linearsearch_recursive(array,9,-1))