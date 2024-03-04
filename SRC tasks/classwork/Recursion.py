def binarySearchResucrsive(arr,item):
    if len(arr) == 1:
        if arr[0] == item:
            return 0
        else:
            return -1
    else:
        mid = len(arr) // 2 - 1
        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            return binarySearchResucrsive(arr[0:mid], item)
        else:
            return binarySearchResucrsive(arr[mid+1:], item)
        # end if
    # end if
# end function

