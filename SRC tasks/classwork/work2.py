student1t = ("Dave","Bloggs",18,True) #ordered
student2t = ("Fred","Smith",True,16) #ordered
def addone(x):
    x = x + 1
    return x
#end function
class Student_record:
    def __init__(self):
        self.age = 0
        self.firstname = ""
        self.lastname = ""
        self.registered = False 
    #end constructor
#end class
student1 = Student_record()
print(student1.age)
student1.firstname = "Dave"
student1.lastname = "Bloggs"
student1.age = 18
student1.registered = True
student2 = Student_record()
student2.firstname = "Fred"
student2.lastname = "Smith"
student2.age = 16
student2.registered = False
print(student1.age,student1.lastname)
print(student1t[2])
newage = addone(student2.age)
print(newage)
print(student2.age)
