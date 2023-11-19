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
My promlems with this exercise:
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

