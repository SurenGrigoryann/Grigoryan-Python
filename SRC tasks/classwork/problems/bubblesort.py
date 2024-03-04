arr = [7,4,6,8,1,5]

def swap(a,b,arr):
    temp = arr[b]
    arr[b] = arr[a]
    arr[a] = arr[b]
# end procedure
    
swap(0,1,arr)
print(arr)

