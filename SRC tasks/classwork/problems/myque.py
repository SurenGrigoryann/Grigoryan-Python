# Initialize queue 

max_size = 5
q1 = [0 for _ in range(max_size)]
q1_size = 0
q1_fp = 0
q1_rp = -1
size = 0


def isempty():
    global q1_size
    return q1_size == 0


def isfull():
    global q1_size, max_size
    return q1_size == max_size
# end function

def enqueue(item):
    global q1_rp, max_size, q1_size
    if not isfull():
        q1_rp = (q1_rp + 1) % max_size
        q1_size = q1_size + 1
        q1[q1_rp] = item
    else:
        print('It is full you cannot add items!')
    # end if
# end procedure


def dequeue():
    global q1_fp,size,max_size,size
    if not isempty():
        item_p = q1_fp
        q1_fp = (q1_fp + 1) % max_size
        size = size - 1
        return q1[item_p]
    # end if
# end function


for num in range(11,16):
    enqueue(num)
#next num
print(q1)
enqueue(16)
print(q1)
for _ in range(6):
    print(dequeue())
#next _
print(q1)
enqueue(20)
print(q1)