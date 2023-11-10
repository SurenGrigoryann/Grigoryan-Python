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
        print(self.color)

    def get_name(self):
        print(self.name)

# Create instances of the Dog class with names and initial colors
myDog3 = Dog('Mutt', 'Unknown')
myDog4 = Dog('Jeff', 'Unknown')

if myDog3.color == 'Unknown':
    myDog3.set_color()
    myDog3.get_color()
    myDog3.get_name()

myDog4 = Dog
myDog4.name = 'Jeff'
myDog4.color = 'Unkown'

if myDog3.color == 'Unkown':
    myDog3.set_color()
    myDog3.get_color()
    myDog3.get_name()
