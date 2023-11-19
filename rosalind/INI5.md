So for this exercise I created the script INI5.py, it contains this code:
```python
f = open("rosalind_ini5.txt", "r")
data = f.readlines()
i = 0
for line in data:
    if i % 2 == 1:
        print(line.strip())
    i = i + 1
``` 
So I first opened the .txt file and saved it as the variable f.\
Next I saved all the lines of the file in data as a list.\
Then I defined i as 0, representing the index of the first line. I then iterated over all the lines and only printed the ones, that had an uneven index using modulo. In rosalind the even lines were asked, but since there they started counting with 1, all their even lines are uneven in python, which starts counting at 0.\
Finally i added .strip() to the end of the line, so that second \n would be removed and so that I wouldn't get an empty line after each correct one.