"""With iteration"""
# def Fib(n):
#     a = 1
#     b = 1
#     if n == 1 or n == 2:
#         return a
#     else:
#         for i in range(n-1):
#             c = a + b
#             a = b
#             b = c 
#         return c

# print(Fib(1))

fibdict = [1,1]

def fib(n):
    if n in fib_dic:
        return fib_dic[n]
    else:
        if n <=1:
            fib_dic[n] = 1
            return 1
        else:
            fib_dic[n] = fib(n-1) + fib(n-2)
            return (fib(n-1)+fib(n-2))
        # end if
    # end if
# end function
        
fib_dic = {}
print(fib(12))
print(fib_dic)

        

        

