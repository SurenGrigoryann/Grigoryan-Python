class Dog():
    def __init__(self, myName, myColor):
        self.name = myName
        self.color = myColor

    def bark(self, barkTimes):
        for i in range(barkTimes):
            print('Woof!')

    def set_color(self):
        color = input('Enter the color > ')
        self.color = color

    def get_color(self):
        return self.color

    def get_name(self):
        return self.name

# Create instances of the Dog class with names and initial colors
myDog3 = Dog('Mutt', 'Unknown')
myDog4 = Dog('Jeff', 'Unknown')

if myDog3.color == 'Unknown':
    print(myDog3.set_color())
    print(myDog3.get_color())
    print(myDog3.get_name())
# end if

class Puppy(Dog):
    super
    def __init__(self,shoesChewed):
        self.shoesChewed = shoesChewed
    # end function

    def chewShoe(self,numShoes):
        self.shoesChewed += numShoes
    # end function

    def getShoesChewed(self):
        print(self.shoesChewed)

myPuppy1 = Puppy(0)

for i in range(4):
    myPuppy1.chewShoe(1)

myPuppy1.get_name()
myPuppy1.getShoesChewed()