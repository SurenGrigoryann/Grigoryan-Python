list = [['x'for i in range(4)] for i in range(6)]
a = 0
b = 0
print(list)

def draw(rowx,column):
    list[column][rowx] = 'O'
    for row in list:
        for item in row:
            print(item, end = ' ')
        print()
    list[column][rowx] = 'x'
    return ''

print(draw(a,b))

coordinate_x = int(input('Your coordinate x > '))
coordinate_y = int(input('Your coordinate y > '))

a = coordinate_x
b = coordinate_y 

print(draw(a,b))