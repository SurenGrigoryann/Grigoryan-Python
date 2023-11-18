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
print(myList)





