lst = []
for i in range(100):
    lst.append(0)

def fib_rab(n, m):
    if n > 2:
        return find_fib_rab(n-1, m) + find_fib_rab(n-2, m) - find_fib_rab(n-(1+m), m)
    elif n < 0:
        return 0
    else:
        return 1
    
def find_fib_rab(n, m):
    if lst[n] == 0:
        lst[n] = fib_rab(n, m)
    return lst[n]
        
print(fib_rab(87,20))