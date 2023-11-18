linked_list = []
def AddItem(newItem):
    if linked_list is full and if so, print error message
    else 
        myList[nextfree].name = newName
        if start = null then
            temp = myList[nextfree].pointer       //save pointer
            myList[nextfree].pointer = null
            start = nextfree
            nextfree = temp
        else
            p = start
            if newName < myList[p].name then  
                myList[nextfree].pointer = start
                start = nextfree
            else    
                placeFound = false    // general case
                while myList[p].pointer <> null and placeFound = false
                    //peek ahead
                    if newName >= myList[myList[p].pointer].name then
                        p = myList[p].pointer
                    else
                        placefound = True
                    endif
                endwhile
                temp = nextFree
                nextfree = node[nextfree].pointer
                node[temp].pointer = node[p].pointer
                node[p].pointer = temp
            endif
        endif
    endif
endprocedure