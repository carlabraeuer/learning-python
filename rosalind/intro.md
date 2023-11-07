## rosalind homework

### **INI1:** 
This first excercise was fairly simple. At first i panicked because it said I only had 5min, but then I downloaded the dataset and followed the one simple instruction of typing ```python import this ``` into the JupyterLab.
I got the poem as output and copy-pasted it to rosalind. The answer was correct.

### **INI2:** 
Reading this exercise I remembered we did pythagoras in mondays lesson, so I went back to my console, which I copied into a text file and looked for the command. Because apparently I can't read tho I replicated the exact code, which of course gave me the wrong output since it gave me the root of the integer. I realized that and changed my code correspondingly. It then looked like this:
```python
def pythagoras_square(a, b):
    c = (a**2 + b**2)
    return c

example pythagoras_square(a, b)
print(example)
```
Then I started the exercise and downloaded the dataset and got **919 866**. I exchanged **a** and **b** of the second part of my code with those numbers. Then because apparently I also can't write, it gave me an error. I realized i missed the "=", so I added that. The final code looked like this:
```python
def pythagoras_square(a, b):
    c = (a**2 + b**2)
    return c

example = pythagoras_square(919, 866)
print(example)
```
As a result I got **1594517** which I copy-pasted to rosalind. The answer was correct.

### **INI3:**
When I saw that we needed to slice stuff I went back to the holy python website and looked at exercise 17. Trying it out with the example I then (after getting a few errors like *TypeError: can only concatenate list (not "str") to list* because I didn't define lst as a space and just wrote ```python s[1:2] + " " + s[4:5] ``` or *NameError: name '...' is not defined* when forgetting the quotation marks) wrote this command in my console:
```python
s = "xxx"
lst = " "

a = x
b = x
c = x
d = x

solution = s[a:b+1] + lst + s[c:d+1]
print(solution)
```
I then started the exercise and downloaded the dataset, I got:
**HD3fRxVYxBCTV9ypWwOMinipterusigKm59eL21wkXsOWDdUXMJNIMipUC7bmFvIKroOnDyLd74hBl58iPbKa2M9lc4KORTuVi5Ic7TVCSOZVB59NcS6f6IZylcbz84fargali1a1WQA8AXOiHrabX7wBkOeZnjFu5OF4eY8.
19 28 128 133** 
I copied the string and replaced the **xxx** with it and defined the variables **a, b, c, d** with the integers respectively.
It looked like this:
```python
s = "HD3fRxVYxBCTV9ypWwOMinipterusigKm59eL21wkXsOWDdUXMJNIMipUC7bmFvIKroOnDyLd74hBl58iPbKa2M9lc4KORTuVi5Ic7TVCSOZVB59NcS6f6IZylcbz84fargali1a1WQA8AXOiHrabX7wBkOeZnjFu5OF4eY8."
lst = " "

a = 19
b = 28
c = 128
d = 133

solution = s[a:b+1] + lst + s[c:d+1]
print(solution)
```
As a result I got **Minipterus argali** which I copy-pasted to rosalind. The answer was correct.


