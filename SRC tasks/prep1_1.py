num = [0,0,0,0,0,0]
num1 = [0 for _ in range(6)]
for i in range(6):
    num[i] = input('Your num > ')
# next i 
for i in range(6):
    print(num[len(num) - i-1])