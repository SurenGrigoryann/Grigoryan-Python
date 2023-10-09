MAX = 10
name_array = ['' for _ in range(MAX)]
name_array[MAX-MAX] = 'suren'
i = 0
yes_no = False
name = input('Your name > ')

while yes_no == False:
    if MAX > i:
        print('There is no such a name!')
        yes_no = True
    else:
        if name_array[i] == name:
            print(f'There is the {name} ')
            yes_no = True
        
