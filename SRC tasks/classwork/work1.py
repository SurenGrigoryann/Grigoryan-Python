RED1 = [255,0,0]
RED2 = (255,0,0)
for i in range(len(RED1)):
    print('RED1',i,RED1[i])
for i in range(len(RED2)):
    print('RED2',i,RED2[i])
RED1[2] = 75
for i in range(len(RED1)):
    print('RED1',i,RED1[i])
RED2[2] = 75
for i in range(len(RED2)):
    print('RED2',i,RED2[i])
    