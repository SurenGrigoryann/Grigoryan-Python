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
start = 0
nextfree = 0
linked_list = []
#print(myList)

def isFull():
    counter = 0
    not_full = 0
    while not_full == 0 and counter != len(myList):
        if myList[counter] != "":
            counter += 1
        else:
            not_full == 1
    if not_full == 0:
        return False
    else:
        return True

def AddItem(newItem,myList):
    global nextfree
    global start

    if isFull():
        print('error message') 
    else: 
        myList[nextfree].name = newItem
        if start == 0:
            temp = myList[nextfree].pointer       
            myList[nextfree].pointer = -1
            start = nextfree
            nextfree = temp
        else:
            p = start
            if newItem < myList[p].name:  
                myList[nextfree].pointer = start
                start = nextfree
            else:    
                placeFound = False
                while myList[p].pointer == -1 and placeFound == False:
                    if myList[p].pointer == -1:
                        if newItem > myList[p].name:
                            myList[nextfree].name = newItem
                            myList[nextfree].pointer = -1
                            myList[p].pointer =  nextfree
                            nextfree += 1
                            placeFound = True
                            
                        else:
                            myList[nextfree].name = newItem
                            myList[nextfree].pointer = p
                            nextfree += 1
                            placeFound = True


                    if newItem >= myList[myList[p].pointer].name:
                        p = myList[p].pointer
                    else:
                        placeFound = True
            #        endif
            #   endwhile
                temp = nextfree
                nextfree = myList[nextfree].pointer
                myList[temp].pointer = myList[p].pointer
                myList[p].pointer = temp
            #endif
        #endif
    #endif
#endprocedure


AddItem("Colin",myList)
AddItem("Albert",myList)
AddItem("Barry",myList)
AddItem("Derek",myList)
AddItem("Fred",myList)
#outputList(myList)
AddItem("Trevor",myList)

print(myList)