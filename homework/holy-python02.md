## 8. For Loop Exercises
```python
#a. Write a for loop so that every item in the list is printed.
for x in lst:
    print(x)

#b. Write a for loop which print "Hello!, " plus each name in the list. i.e.: "Hello!, Sam"
lst=["Sam", "Lisa", "Micha", "Dave", "Wyatt", "Emma", "Sage"]
for x in lst:
    print("Hello!, " + x)

#c. Write a for loop that iterates through a string and prints every letter.
str="Antarctica"
for x in str:
    print(x)
#first thought it was more complicated and used str[x]

#d. Type a code inside the for loop so that counter variable named c is increased by one each time loop iterates. Can you guess how many times it will add 1?.
#will add one less than the number of characters
str="Civilization"
c=0
for i in str:
    c = c + 1
print(c)

#this option shows all the values c has during the loop, shows how often +1 is added to c
for i in str:
    print(c)
    c = c + 1

#e. Using a for loop and .append() method append each item with a Dr. prefix to the lst.
lst1=["Phil", "Oz", "Seuss", "Dre"]
lst2=[]
for x in lst1:
    lst2.append("Dr. " + x)
print(lst2)

#f. Write a for loop which appends the square of each number to the new list.
lst1=[3, 7, 6, 8, 9, 11, 15, 25]
lst2=[]
for x in lst1:
    lst2.append(x**2)
print(lst2)

#g. Write a for loop using an if statement, that appends each number to the new list if it's positive.
lst1=[111, 32, -9, -45, -17, 9, 85, -10]
lst2=[]
for x in lst1:
    if x > 0:
        lst2.append(x)
print(lst2)

#h. Using for loop and if statement, append the value minus 1000 for each key to the new list if the value is above 1000. i.e.: if the value is 1500, 500 should be added to the new list.
dict={"z1":900, "t1": 1100, "p1": 2300, "r1": 1050, "k1": 3200, "g1": 400}
lst=[]
for x in dict:
    if x > 1000:
        lst.append(dict[x]-1000)
print(lst)
#needed hint 2 for the dict[x]

#i. Write a for loop which appends the type of each element in the first list to the second list.
lst1=[3.14, 66, "Teddy Bear", True, [], {}]
lst2=[]
for x in lst1:
    lst2.append(type(x))
print(lst2)
#needed to look up command type 😅
```
