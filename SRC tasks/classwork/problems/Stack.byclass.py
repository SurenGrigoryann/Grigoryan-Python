class Stack:
    def __init__ (self,size) -> None:
        self.maxSize = size
        self.data = ['' for _ in range(size)]
        self.sp = -1
    # end cunstroctur

    def size(self):
        return self.sp + 1
    # end function

    def isFull(self):
        return self.size() == self.maxSize
    # end function

    def isEmpty(self):
        return self.sp == -1
    # end function    

    def push(self, item):
        if self.isFull():
            print('Stack is full!')
        else:
            self.sp += 1
            self.data[self.sp] = item
        # end if
    # end procedure
     
    def pop(self):
        if self.isEmpty():
            print('Stack is Empty!')
        else:
            self.sp -= 1
            return self.data[self.sp + 1]
        # end if
    # end function
        
    def peek(self):
        if self.isEmpty():
            print('Stack is Empty!')
        else:
            return self.data[self.sp]
        # end if
    # end function


    

myString = input('Input your word > ')

numChars = len(myString)
s = Stack(numChars)

for c in myString:
    s.push(c)

reverseword = ''


if s.isEmpty() == -1:
    print('Stack is empty!')
else:
    top =len(s.data) - 1
    reverseword += ((s.data[top]))
    for i in range(top-1,-1,-1):
        reverseword += (s.data[i])


if reverseword == myString:
    print('It is palindrome')
else:
    print('it is not palindrome')