class Node:
    def __init__(self,name,pointer) -> None:
        self.name = name
        self.pointer = pointer
    #end constructor
    def __repr__(self) -> str:
        return "Data:"+self.name+",Ptr:"+str(self.pointer)
#end Node record
# Create array of blank Nodes (records)
myList = [Node("",-1) for _ in range(50) ]
for index in range(49):
    myList[index].pointer = index + 1
#next index
myList[49].pointer = -1
start = -1
nextfree = 0
linked_list = []

# Is Full Function
def isFull():
    counter = 0
    not_full = 0
    while not_full == 0 and counter != len(myList):
        if myList[counter] != "":
            counter += 1
        else:
            not_full == 1
        # end if
    # end while
    if not_full == 0:
        return False
    else:
        return True
    # end if
# end function


# is empty function
def isEmpty():
    empty = 1
    for i in range(len(myList)):
        if i != "":
            empty = 0
        # end if
    # next i
    if empty == 0:
        return False
    elif empty == 1:
        return True
    # end if
# end function

# adding item procedure
def addItem(item):
    global start
    global nextfree
    global myList
    counter = 0
    found_place = False
    find_item = 0
    if isFull():
        print('error message')
    elif isEmpty():
        myList[0] = item
        nextfree = 1
        start = 0
        myList[0].pointer = -1
    else:
        temp = start
        while not found_place:
            if myList[temp] > item:
                if myList[temp] == myList[start]:
                    myList[nextfree] = item
                    myList[nextfree].pointer = temp
                    start = nextfree
                    found_place = True        
                temp = myList[temp].pointer
            elif myList[temp].pointer == -1 and item > myList[temp]:
                myList[nextfree] = item
                myList[nextfree].pointer = -1
                myList[temp].pointer = nextfree
            else:
               pass