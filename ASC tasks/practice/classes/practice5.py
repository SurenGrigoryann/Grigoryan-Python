class Cat():
    def __init__(self):
        self.weight = 0
        self.color = ''
        self.name = ''
    
    def meow(self):
        print(self.name,'says meow')

class Monster():
    def __init__(self):
        self.name = ''
        self.health = int

    def decrease_health(self,amount):
        self.health = self.health - amount 
        if self.health <= 0 :
            death = f'{self.name} died'
            return death

        else:
            print(self.name,'is alive')
            return self.health

my_cat = Cat()
my_cat.weight = 12
my_cat.color = 'black'
my_cat.name = 'Ashot'

print(my_cat.weight)
print(my_cat.meow())

my_monster = Monster()
my_monster.name = 'Ashot'
my_monster.health = 150

damage = int(input('Your damage > '))
print(my_monster.decrease_health(damage))