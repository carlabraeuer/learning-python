ipython

In [1]: s = "the quick brown fox jumps over the lazy dog"

In [2]: words = s.split()

In [3]: words
Out[3]: ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

In [4]: words[3]
Out[4]: 'fox'

In [5]: words[3][2]
Out[5]: 'x'

In [6]: cities = ["Vienna", "Dublin", "Udine", "New York", "Los Angeles"]

In [7]: cities.append("London")

In [8]: cities[2]
Out[8]: 'Udine'

In [9]: exit

#in INI4.py:
a = 1
b = 100

#the sum from all odd integers from a through b, inclusively

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
#

#in bash
python INI4.py

