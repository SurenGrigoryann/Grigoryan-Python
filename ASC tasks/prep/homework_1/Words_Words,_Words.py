text = input('your text > ')
# geting the text from user

#assuming that the user typed a ' ' after every word 
# so we need to calculate how many ' ' are there and +1 to get the number of words
prabel = 0

for i in range(len(text)):
    if text[i] ==' ':
        prabel += 1
    
print(f'{prabel + 1} words')