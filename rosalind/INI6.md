**Since I missed class on friday, I didn't see Monica's solution, but here is mine. Trying to explain it as good as possible!**

Here is my code and my output:
```python
zen = "We tried list and we tried dicts also we tried Zen"
​
zen = zen.split()
​
dict = {}
​
for word in zen:
    dict[word] = zen.count(word)
    
for key, value in dict.items():
    print(key, value)
We 1
tried 3
list 1
and 1
we 2
dicts 1
also 1
Zen 1
```
So first I saved the dataset as a value. I then overrode said value with a list containing all the single words from the dataset. To do this I used the first hint from rosalind, the .split() command.\
Then I created an empty dictionary to later save my key-value pairs in.\
With a for-loop to iterate over all the words in my list I saved the word as key and the count of the word as value in my directory.\
Finally, using the second hint, I printed the pairs of my dictionary, the way it was expected in rosalind.
Because the hint didn't completely fit the expected output, I changed the two print commands into one.

This way worked very good for me, since I could build it step-by-step and with it I could solve the exercise in my first attempt.