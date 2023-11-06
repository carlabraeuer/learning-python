## 1. print()function
```python
#a. Replace "type here" on line 2 with "Hello World!"
print("Hello World!")

#b. You can assign "Hello World!" to the variable below on line 3.
my_text = "Hello World!"
print(my_text)

#c. Type a couple of different values on line 9 inside the print function. Make sure they are separated by commas.
print("hello", "goodbye", "octopus", "pizza")
```


## 2. Variables
```python
#a. Type here. Assign a number to the variable: glass_of_water
glass_of_water = 3
print("I drank", glass_of_water, "glasses of water today.")

#b. Fill the print function so it prints glass_of_water
glass_of_water = 3
glass_of_water = glass_of_water + 1
print(glass_of_water)
```


## 3. Data Types
```python
#a. Assign an integer to the variable, then print it.
men_stepped_on_the_moon = 12
print(men_stepped_on_the_moon)

#b. Type a couple of words or a short sentence for your variable, then print it.
my_reason_for_coding = "trying hard to be cool"
print(my_reason_for_coding)

#c. Assign a float with 2 decimals to the variable below. If you don't wan't to search the value you can check out Hint 1.
global_mean_sea_level_2018 = 21
#Type your code here.
global_mean_sea_level_2018 = 21.36
print(global_mean_sea_level_2018)

#d. Assign True or False to the variable below then print it.
staying_alive = False
print(staying_alive)
```


## 4. Type Conversion
```python
#a. Using type() function assign the type of the variable to answer_1, then print it.
men_stepped_on_the_moon = 12
#Type your code here.
answer_1 = type(men_stepped_on_the_moon)
print(answer_1)

#b. Using type() function assign the type of the variable to answer_2, then print it.
my_reason_for_coding = "intergalactic travel"
#Type your code here.
answer_2 = type(my_reason_for_coding)
print (answer_2)

#c. Using type() function assign the type of the variable to answer_3, then print it.
global_mean_sea_level_delta_2018 = 21.36
#Type your code here.
answer_3 = type(global_mean_sea_level_delta_2018)
print(answer_3)

#d. print the type of boolean data
staying_alive = True
#Type your code here.
answer_4 = type(staying_alive)
print(answer_4)

#e. my_grade variable is a string (because it's in quotes). On line 9, convert it to an integer.
my_grade = "10"
answer_5 = int(my_grade)
print(answer_5)

#f. my_temp variable is a float (because it has decimals). On line 9, convert it to an integer.
my_temp = 97.70
answer_6 = int(my_temp)
print(answer_6)

#g. shoe_price variable is a string (because it's in quotes). On line 9, convert it into a float.
shoe_price = "69.99"
answer_7 = float(shoe_price)
print(answer_7)

#h. GWP denotes the total economic activity created by the world population collectively in a year.
gross_world_product = 84.84
gwp_str = str(gross_world_product)
answer_8 = "In 2018 gross product of the world (GWP) was " + gwp_str + " in 
trillion US dollars."
print(answer_8)
```


## 6. Lists
```python
#a. Assign the first element of the list to answer_1 on line 2
lst = [11, 100, 99, 1000, 999]
answer_1 = lst[0]
print(answer_1)

#b. This time print the second element of the list directly on line 3. You should get 100.
lst = [11, 100, 101, 999, 1001]
print(lst[1])

#c. Print the last element of the list through variable answer_1.
lst = [11, 100, 101, 999, 1001]
#Type your answer here.
answer_1 = lst[-1]
print(answer_1)

#d. On line 3, add the string "pajamas" to the list with .append() method.
gift_list = ['socks', '4K drone', 'wine', 'jam']
#Type your code here.
gift_list.append("pajamas")
print(gift_list)

#e. On line 3, this time add the sub-list: ["socks", "tshirt", "pajamas"] to the end of the gift_list.
gift_list = ['socks', '4K drone', 'wine', 'jam']
#Type your code here.
gift_list.append(["socks", "tshirt", "pajamas"])
print(gift_list)

#f. On line 3, this time insert "slippers" to index 3 of gift_list.
gift_list = ['socks', '4K drone', 'wine', 'jam']
#Type your code here
gift_list.insert(2, "slippers")
print(gift_list)

#g. With .index() method you can learn the index number of an item inside your list. Assign the index no of 8679 to the variable answer_1.
lst = [55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]
#Type your code here.
answer_1 = lst.index(8679)
print(answer_1)

#h. Using .append() method, add a new list to the end of the list which contains strings: "Navigator" and "Suburban".
lst = ["CRV", "Outback", "XC90", "GL", "Cherokee", "Escalade"]
#Type your code here.
lst.append(["Navigator", "Suburban"])
print(lst)

#i. Using .remove() method, clear the last element of the list.
lst = [55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]
#Type your code here.
lst.remove(lst[-1])
print(lst)

#j. Using .reverse() method, reverse the list.
lst = [55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]
#Type your code here.
lst.reverse()
print(lst)

#k. Using .count() method, count how many times 6 occur in the list.
lst = [55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
#Type your code inside print() function.
answer_1 = lst.count(6)
print(answer_1)

#l. What is the sum of all the numbers in the list?
lst = [55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
#Type your code on line 4:
answer_1 = sum(lst)
print(answer_1)

#m. What is the minimum value in the list?
lst = [55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
#Type your code on line 4:
answer_1 = min(lst)
print(answer_1)

#n. What is the maximum value in the list?
lst = [55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
#Type your code on line 4:
answer_1 = max(lst)
print(answer_1)
```


## 9. Strings
```python
#a. Assign the string below to the variable in the exercise.
#Type your answer here.
str = "It's always darkest before dawn."
print(str)

#b. By using first, second and last characters of the string, create a new string.
str = "It's always darkest before dawn."
#Type your answer here.
ans_1 = str[0] + str[1] + str[-1]
print(ans_1)

#c. Replace the (.) with (!)
str="It's always darkest before dawn."
#Type your code here.
str = str.replace(".", "!")
print(str)

#d. Reassign str so that, all its characters are lowercase.
str = "EVERY Strike Brings Me Closer to the Next Home run."
#Type your code here.
str = str.lower()
print(str)

#e. Now make everything uppercase.
str = "don't stop me now."
#Type your code here.
str = str.upper()
print(str)

#f. Make the string so that everything is properly and first letter is capital with one function.
str = "there are no traffic JamS Along The extra mile."
#Type your answer here.
str = str.capitalize()
print(str)

#g. Does the string start with an A? Assign a boolean answer to the ans_1 variable.
str = "There are no traffic jams along the extra mile."
#Type your code here.
ans_1 = str.startswith("A")
print(ans_1)

#h. Does it end with a fullstop (.) ?
str = "There are no traffic jams along the extra mile."
#Type your code here.
ans_1 = str.endswith(".")
print(ans_1)

#i. Using .index() method, identify the index of character: (v).
str = "The best revenge is massive success."
#Type your code here.
ans_1 = str.index("v")
print(ans_1)

#j. Using .find() method, identify the index of character: (m).
str = "The best revenge is massive success."
#Type your code here.
ans_1 = str.find("m")
print(ans_1)

#k. Try to see what results you get looking for character: (X). First with .find() method and then with .index() method.
str = "The best revenge is massive success."
#Type your code here.
#find -> better, returns -1
ans_1 = str.find("X")
print(ans_1)
#index -> doesn't return something
ans_1 = str.index("X")
print(ans_1)

#l. Which character occur more often in the string? "a" or "o" ? Print both counts inside the print function.
str = "People often say that motivation doesn't last. Well, neither does bathing.  That's why we recommend it daily."
#Type your code here.
ans_1 = str.count("a")
ans_2 = str.count("o")
print("count of a is: ", ans_1, " count of o is: ", ans_2)

#m. Print the types of two given variables with the print function.
v_1 = "1"
v_2 = 1
#Type your code on line 4:
ans_1 = type(v_1)
ans_2 = type(v_2)
print(ans_1)
print(ans_2)

#n. What is the length of the given string?
str = "1.975.000"
#Type your code here:
ans_1 = len(str)
print(ans_1)
```


## 11. .sort()method
```python
#a. Sort the list in ascending order with .sort() method.
lst = [11, 100, 99, 1000, 999]
#Type your answer here.
lst.sort()
print(lst)

#b. This time sort the countries in alphabetic order.
lst = ["Ukraine", "Japan", "Canada", "Kazakhstan", "Taiwan", "India", "Belize"]
#Type your code here
lst.sort()
print(lst)

#c. Now sort the list in descending order with .sort() method.
lst = [11, 100, 101, 999, 1001]
#Type your answer here.
lst.sort(reverse = True)
print(lst)

#d. Can you sort the gift list in reverse alphabetic order?
gift_list = ['socks', '4K drone', 'wine', 'jam']
#Type your answer here.
gift_list.sort(reverse = True)
print(gift_list)

#e. Sort the list below in reverse alphabetic order and then assign the last element to the answer_1 variable.
NFL = ["Panthers", "Bears", "Dolphins" "Patriots", "Saints", "Giants"]
#Type your code here.
NFL.sort(reverse = True)
answer_1 = NFL[-1]
print(answer_1)

#f. Sort the cities from z to a.
muni = ["Melbourne", "Shanghai", "Delhi", "Atlanta", "Moscow", "Montreal"]
# Type your code here.
muni.sort(reverse = True)
print(muni)
```


## 12. .pop()method
```python
#a. Pop the last item of the list below.
lst = [11, 100, 99, 1000, 999]
#Type your answer here.
popped_item = lst.pop()
print(popped_item)
print(lst)

#b.
lst = ["milk", "banana", "eggs", "bread", "broccoli", "lemons"]
#Type your code here.
item = lst.pop(lst.index("broccoli"))
print(lst, item)
```


## 17. Slicing Notation
```python
#a.


#b.


#c.


#d.


#e.


#f.


#g.


#h.

``
