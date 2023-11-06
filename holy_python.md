## 1. print()function
```python
#Replace "type here" on line 2 with "Hello World!"
print("Hello World!")

#You can assign "Hello World!" to the variable below on line 3.
my_text = "Hello World!"
print(my_text)

#Type a couple of different values on line 9 inside the print function. Make 
sure they are separated by commas.
print("hello", "goodbye", "octopus", "pizza")
```


##2. Variables
'''python
#Type here. Assign a number to the variable: glass_of_water
glass_of_water = 3
print("I drank", glass_of_water, "glasses of water today.")

#Fill the print function so it prints glass_of_water
glass_of_water = 3
glass_of_water = glass_of_water + 1
print(glass_of_water)
'''


##3. Data Types
'''python
#Assign an integer to the variable, then print it.
men_stepped_on_the_moon = 12
print(men_stepped_on_the_moon)

#Type a couple of words or a short sentence for your variable, then print it.
my_reason_for_coding = "trying hard to be cool"
print(my_reason_for_coding)

#Assign a float with 2 decimals to the variable below. If you don't wan't to 
search the value you can check out Hint 1.
global_mean_sea_level_2018 = 21
#Type your code here.
global_mean_sea_level_2018 = 21.36
print(global_mean_sea_level_2018)

#Assign True or False to the variable below then print it.
staying_alive = False
print(staying_alive)
'''


##4. Type Conversion
'''python
# Using type() function assign the type of the variable to answer_1, then print 
it.
men_stepped_on_the_moon = 12
#Type your code here.
answer_1 = type(men_stepped_on_the_moon)
print(answer_1)

#Using type() function assign the type of the variable to answer_2, then print 
it.
my_reason_for_coding = "intergalactic travel"
#Type your code here.
answer_2 = type(my_reason_for_coding)
print (answer_2)

#Using type() function assign the type of the variable to answer_3, then print 
it.
global_mean_sea_level_delta_2018 = 21.36
#Type your code here.
answer_3 = type(global_mean_sea_level_delta_2018)
print(answer_3)

#print the type of boolean data
staying_alive = True
#Type your code here.
answer_4 = type(staying_alive)
print(answer_4)

#my_grade variable is a string (because it's in quotes). On line 9, convert it 
to an integer.
my_grade = "10"
answer_5 = int(my_grade)
print(answer_5)

#my_temp variable is a float (because it has decimals). On line 9, convert it to 
an integer.
my_temp = 97.70
answer_6 = int(my_temp)
print(answer_6)

#shoe_price variable is a string (because it's in quotes). On line 9, convert it 
into a float.
shoe_price = "69.99"
answer_7 = float(shoe_price)
print(answer_7)

#GWP denotes the total economic activity created by the world population 
collectively in a year.
gross_world_product = 84.84
gwp_str = str(gross_world_product)
answer_8 = "In 2018 gross product of the world (GWP) was " + gwp_str + " in 
trillion US dollars."
print(answer_8)
'''


##6. Lists
'''python
#Assign the first element of the list to answer_1 on line 2
lst = [11, 100, 99, 1000, 999]
answer_1 = lst[0]
print(answer_1)

#This time print the second element of the list directly on line 3. You should 
get 100.
lst = [11, 100, 101, 999, 1001]
print(lst[1])

#Print the last element of the list through variable answer_1.
lst = [11, 100, 101, 999, 1001]
#Type your answer here.
answer_1 = lst[-1]
print(answer_1)

#On line 3, add the string "pajamas" to the list with .append() method.
gift_list = ['socks', '4K drone', 'wine', 'jam']
#Type your code here.
gift_list.append("pajamas")
print(gift_list)

#On line 3, this time add the sub-list: ["socks", "tshirt", "pajamas"] to the 
end of the gift_list.
gift_list = ['socks', '4K drone', 'wine', 'jam']
#Type your code here.
gift_list.append(["socks", "tshirt", "pajamas"])
print(gift_list)

#On line 3, this time insert "slippers" to index 3 of gift_list.
gift_list = ['socks', '4K drone', 'wine', 'jam']
#Type your code here
gift_list.insert(2, "slippers")
print(gift_list)

#With .index() method you can learn the index number of an item inside your 
list. Assign the index no of 8679 to the variable answer_1.
lst = [55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]
#Type your code here.
answer_1 = lst.index(8679)
print(answer_1)

#Using .append() method, add a new list to the end of the list which contains 
strings: "Navigator" and "Suburban".
lst = ["CRV", "Outback", "XC90", "GL", "Cherokee", "Escalade"]
#Type your code here.
lst.append(["Navigator", "Suburban"])
print(lst)

#Using .remove() method, clear the last element of the list.
lst = [55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]
#Type your code here.
lst.remove(lst[-1])
print(lst)

#Using .reverse() method, reverse the list.
lst = [55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]
#Type your code here.
lst.reverse()
print(lst)

#Using .count() method, count how many times 6 occur in the list.
lst = [55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
#Type your code inside print() function.
answer_1 = lst.count(6)
print(answer_1)

#What is the sum of all the numbers in the list?
lst = [55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
#Type your code on line 4:
answer_1 = sum(lst)
print(answer_1)

#What is the minimum value in the list?
lst = [55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
#Type your code on line 4:
answer_1 = min(lst)
print(answer_1)

#What is the maximum value in the list?
lst = [55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
#Type your code on line 4:
answer_1 = max(lst)
print(answer_1)
'''


##9. Strings
