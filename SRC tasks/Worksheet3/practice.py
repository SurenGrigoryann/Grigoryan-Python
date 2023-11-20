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
start = 1
nextfree = -1
linked_list = []


def addItem(item):
    global start
    global nextfree
    global myList
    counter = 0
    found_place = 0
    find_item = 0
    while counter <= len(myList) and find_item == 0:
        if myList[counter] != "":
            find_item = counter      
        
        elif counter == len(myList):
            myList[0] = item
            myList[0].pointer = -1
            start = 0
            nextfree = 1

    if find_item != 0:
        if item > myList[counter]:
            while found_place == 0:
                if item > myList[counter] :
                    pass