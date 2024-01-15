#FIBD

#old 13.12.23
#def fib(n):
#    if n > 1:
#        return fib(n-1) + fib(n-2)
#    else:
#        return 1
#
#for i in range(10):
#    print(fib(i))

#new 14.01.24
def fib_rab(n, k):
    if n > 2:
        return fib_rab(n-1, k) + fib_rab(n-2, k) * k
    else:
        return 1
    
print(fib_rab(35, 5))