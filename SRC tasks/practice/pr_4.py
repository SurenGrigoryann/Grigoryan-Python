s = 'suren'
numChar = len(s)

Stack = []

for i in range(numChar):
    Stack.append(s[numChar - i - 1])
    i += 1

print(Stack)