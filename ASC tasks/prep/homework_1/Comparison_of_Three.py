num_1 = int(input('your first number > '))
num_2 = int(input('your second number > '))
num_3 = int(input('your third number > '))
# inputing three numbers

if num_1 >= num_2 and num_1 >= num_3:
    if num_2 > num_3:
        print (num_3,num_2,num_1)
    else:
        print(num_2,num_3,num_1)
    # assuming that num_1 is the greatest
    # end if
elif num_2 >= num_1 and num_2 >= num_3:
    if num_1 > num_3:
        print (num_3,num_1,num_2)
    else:
        print(num_1,num_3,num_2)
    # assuming that num_2 is the greatest
    # end elif
elif num_3 >= num_2 and num_3 >= num_3:
    if num_1> num_2:
        print (num_2,num_1,num_3)
    else:
        print(num_1,num_2,num_3)
    # assuming that num_3 is the greatest
    # end if

# end if