pupils = 20
list_of_pupils = [f'student{_ + 1}'for _ in range(pupils)]

group_1 = ['' for _ in range(pupils//2)]
group_2 = ['' for _ in range(pupils//2)]

group_1_index = 0
group_2_index = 0

for i in range(pupils):
    if i % 2 == 0:
        group_1[group_1_index] = list_of_pupils[i]
        group_1_index += 1
    else:
        group_2[group_2_index] = list_of_pupils[i]
        group_2_index += 1

print(group_1)
print(group_2)