num = int(input('input your number beetwen 100-999 > '))

hundreds = num // 100
tens = (num - (hundreds*100)) // 10
units = (num - (hundreds*100) - (tens * 10))

print(hundreds,'hundreds',tens, 'tens','and',units,'units')

