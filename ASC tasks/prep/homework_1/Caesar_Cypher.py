list_of_num = []
# making a list which we will use later
for i in range(26):
    list_of_num.append(i+97)
    # typing all the alcii numbers in list

length = 0
# we will use this variable later

for i in list_of_num:
    length += 1
    if length >= 25:
        # for the case of z and y
        print(f'{chr(i)} = {chr((list_of_num[-25 + length]))}')
    else:
        print(f'{chr(i)} = {chr(i+2)}')
    # end if