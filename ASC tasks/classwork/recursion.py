# def calc(n):
#     if n == 0:
#         factorial = 1
#     else:
#         factorial = n * calc(n-1)
#     return factorial

# print(calc(998))


numbers = [3,6,2,8,1]
index = len(numbers) -1
all = 0
def sum(list,ind):
    if ind < 0:
        return 0
    else:
        return list[ind] + sum(list,ind-1)



print(sum(numbers,index))