list1 = [34,56,34,26,80,57,98,100,80,64,102,300,35,6,87,88]
index = 0

for i in range(len(list1) - 1):
    index += 1
    if list1[index] >= 80 and list1[index] <= 100:
        item = list1[index]
        list1.remove(item)
        index -= 1

print(list1)
