# My experience with rosalind's DNA exercises

## DNA, counting DNA nucleotides
This exercise was very nice, because I had to use "old" knowledge. Felt very nice to just know something and get the right solution immediately 😅\
All I really needed was the .count() command.\
I solved it like this:
```python
dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
A = dna.count("A")
C = dna.count("C")
G = dna.count("G")
T = dna.count("T")
print(A, C, G, T)
```
To achieve the same output look as rosalind and to give it a clearer look I decided on saving each count as variable and then print them all in one command.\
With this I solved it in my first attempt.

## RNA, transcribing DNA to RNA 
This also was very nice to solve, here the key-command was .replace():
```python
dna = "GATGGAACTTGACTACGTAAATT"
rna = dna.replace("T", "U")
print(rna)
```
With this I solved it in my first attempt.

## REVC, reverse compliment
This again cost me a few more nerves, especially since I couldn't join the friday lesson. 
But with the flow diagram and some help from Barbara's notes I managed to get this solution:
```python
dna = "AAAACCCGGT"
complement = ""
for x in dna:
    if x == "A":
        complement += "T"
    elif x == "T":
        complement += "A"
    elif x == "C":
        complement += "G"
    elif x == "G":
        complement += "C"
reverse = complement[::-1]
print(reverse)
```
With this I solved it in my first attempt.\
.\
**My promlems with this exercise:**
1. I wanted to use the .reverse() but I had to learn, that it doesen't work for strings. Luckily I remembered, that it was possible to slice backwards.
2. I tried to replace one letter after the other but quickly ran into the problem of only ending up with two letters because I accidentally reversed my changes. Here my wrong code and output for reference:
```python
dna = "AAAACCCGGT"
complementA = dna.replace("A", "T")
complementT = complementA.replace("T", "A")
complementC = complementT.replace("C", "G")
complementG = complementC.replace("G", "C")
reverse = complementG[::-1]
print(reverse)

ACCCCCAAAA
```
3. First I wanted to do 4 if-statements but with help of the flow-chart, I realized i needed elif.

## Mofif in DNA
This excercise was discussed in class today, so we solved almost everything together. I ended up with this solution.
```python
dna = "GATATATGCATATACTT"
indices = []

for i in range(len(dna)):
    if dna[i:i+4] == "ATAT":
        indices.append(i + 1)

result = ' '.join(map(str, indices))
print(result)
```
When we realized we needed to splice, i realized, that we would need ``` dna[i:i+4] == "ATAT"```to search for the subsequence "ATAT". Then I struggled a bit. I knew we needed to find a way to get the indices, so after getting the error "TypeError: can only concatenate str (not "int") to str" I realized iterating through dna (as I tried before) was not the right way. So I realized I needed integers responding to the dna-string. I remembered the range(len(dna)) way and it worked :).\
To get the right form of output I created an empty list and then appended the indices + 1 to it ("+1" because python starts at 0 and we start at 1). Then I had them in a row, but like this: ```[2, 4, 10]```. I couldn't come up with a solution, so I asked ChatGPT *how do I get this format of output "2 4 10" when I have a list: "list = [2, 4, 10]"*. It gave me this answer:
```python
my_list = [2, 4, 10]
result = ' '.join(map(str, my_list))
print(result)
```
With this I solved it in my first attempt.
