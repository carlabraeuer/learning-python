a = 1
b = 5

#the sum from all integers from a through b, inclusively
#1st option
result = 0
for n in range(0, b-a+1):
    print("adding new number", n, "to result", result)
    result = result + (a + n)
print(result)

#2nd option
result = 0
for n in range(a, b+1):
    print ("adding new number", n, "to result", result)
    result = result + n

print(result)


#the sum from all odd integers from a through b, inclusively
result = 0
for n in range(a, b+1):
    if n % 2 == 1:
        result = result + n
    else:
        continue
print(result)