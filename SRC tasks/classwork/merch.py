alist = [1, 3, 4, 6, 8, 9,19,20]
blist = [2,5,12,14,17]
clist = [0 for _ in range(len(alist)+len(blist))]


def merge(l1,l2,l3):
    pointer1 = 0
    pointer2 = 0
    pointer3 = 0
    finished1_2 = 0
    finished = False
    while pointer3 != len(l3) and finished == False:
        
        if l1[pointer1] > l2[pointer2]:
            l3[pointer3] = l2[pointer2]
            pointer2 += 1
            pointer3 += 1 
            if len(l2) == pointer2:
                finished = True
                finished1_2 = 2

        elif l1[pointer1] <= l2[pointer2]:
            l3[pointer3] = l1[pointer1]
            pointer1 +=1
            pointer3 += 1 
            if len(l1) == pointer1:
                finished = True
                finished1_2 = 1

        print(l3,pointer3)

    if finished1_2 == 1:
        for i in range(len(l2)- pointer2-1, len(l2)):
            l3[pointer3] = l2[i]
            pointer3 += 1
    elif finished1_2 == 2:
        for i in range(len(l1)- pointer1-1, len(l1)):
            print(l3)
            l3[pointer3] = l1[i]
            pointer3 += 1  
        print('zfas')
        print(l3)
    print(l3)
merge(alist, blist, clist)
