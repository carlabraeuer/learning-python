#FIBD

def fib(n):
    if n > 1:
        return fib(n-1) + fib(n-2)
    else:
        return 1

for i in range(10):
    print(fib(i))