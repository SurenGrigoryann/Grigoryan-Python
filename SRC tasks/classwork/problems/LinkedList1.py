class Node():
    def __init__ (self,data,pointer):
        self.data = data
        self.pointer = pointer
    # end cronstructor
    def __repr__(self) -> str:
        return "Data:"+self.data+",Ptr:"+str(self.pointer)
#end Node record
linked_list_data = []
linked_list_data.append(Node("Lucas",2))
linked_list_data.append(Node("Ayaan",0))
linked_list_data.append(Node("Suren",-1))
linked_list_data.append(Node("Empty",4))
linked_list_data.append(Node("Empty",-1))

start_pointer = 1
next_free_pointer = 3

print(linked_list_data)

def show_right(list,start):
    current_pointer = start

    while current_pointer != -1:
        print(list[current_pointer].data)
        current_pointer = list[current_pointer].pointer
   # end while
# end function

show_right(linked_list_data,start_pointer)


