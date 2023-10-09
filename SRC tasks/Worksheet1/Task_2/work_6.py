from csv import list_dialects


list_of_cars = [['empty' for i in range(10)] for k in range(6)]
#print(list_of_cars)
parked = False


while parked == False:
        type_of_car = input('Your car > ')
        coordinate_y = input("Your row > ")
        coordinate_x = input("Your car's place > ")
    #try:
        coordinate_x = int(coordinate_x)
        coordinate_y = int(coordinate_y)
        if coordinate_y <= 10 and coordinate_y >= 1 and coordinate_x >= 1 and coordinate_x <= 6:
            list_of_cars[coordinate_x -1][coordinate_y - 1] = type_of_car
            for row in list_of_cars:
                    for item in row:
                        print(item, end = ' ')
                    print()
            parked = True
        else:
            print('Invalid input! Try again!')
    
    #except:
     #    print('Invalid input try again!', end = '\n')
