name = ['r','o','b','e','r','t']
stack = []
outname = []

for i in name:
    stack.append(i)

for index in range(0,len(stack)):
    outname.append(stack.pop())

print(outname)