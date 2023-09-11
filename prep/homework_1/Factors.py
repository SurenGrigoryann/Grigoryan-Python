num = int(input('your number > '))
# getting the number from the user

list_of_factors = []
for factor in range(num//2  + 1):
    # diving by two because after that there is no possibility to have factors
    try:
    # doing try because of the fact that factor could be 0 and diving by 0 is not possible
        if num % (factor) == 0:
            list_of_factors.append(factor)
            # appending all the factors
        # end if
    except:
        pass
for factor in list_of_factors:
    print(f'{factor}, ', end = '')
# printing all the factors