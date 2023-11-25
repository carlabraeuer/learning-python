# My experience with rosalind's DNA exercises
Contents: DNA, RNA, REVC, GC, HAMM, SUBS, IPRB, PROT

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

## GC,


## HAMM,Counting point mutations
I did this one quite late so I found it easier to solve!
This is my code:
```python
ham1 = "GAGCCTACTAACGGGAT"
ham2 = "CATCGTAATGACGGCCT"

count = 0

for i in range(len(ham1)):
    if ham1[i] != ham2[i]:
        count = count + 1
print(count)
```
With this I solved it in my first attempt.

## SUBS, Mofif in DNA
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
While solving I realized I needed to exchange 3 items in my code, so i did it like this to make it more generic:
```python
dna_seq = "GATATATGCATATACTT"
sub_seq = "ATAT"
indices = []

for i in range(len(dna_seq)):
    if dna_seq[i:i+len(sub_seq)] == sub_seq:
        indices.append(i + 1)

result = ' '.join(map(str, indices))
print(result)
```

## IPRB, Mendels first law
So this one really did a number on me... I tried breaking it down and drawing it, but used very **wrong** math...\
<img width="495" alt="Screenshot 2023-11-23 at 21 31 08" src="https://github.com/carlabraeuer/learning-python/assets/148707864/f0a28b0e-d11b-476b-a5b7-46c009f9bb58">
.\
From this drawing I came up with this code:
```python
k = 2
m = 2
n = 2

dom = k*4 + m*3 + k*m*n*10
rez = n*4 + m*1 + k*m*n*2

result = dom / (dom+rez)

print(result)
```
Sadly this worked for the rosalind example so I tried it out and got two wrong trys. 
I figured it was because my code only works when k, m and n are the same number.\
When we tried it in class we also broke it down and wrote down the right math.\
Still took me a bit because I still made some wrong turns in math but in the end I made this drawing:\
<img width="548" alt="Screenshot 2023-11-23 at 23 21 36" src="https://github.com/carlabraeuer/learning-python/assets/148707864/2a36ba51-7f51-4c70-8c23-edaf38ba3681">
.\
With it I could figure out the right code:
```python
k = 2
m = 2
n = 2
pop = k + m + n

kk = (k/pop) * (k-1)/(pop-1)
km = (k/pop) * m/(pop-1)
kn = (k/pop) * n/(pop-1)
mk = (m/pop) * k/(pop-1)
mm = (m/pop) * (m-1)/(pop-1) * 0.75
mn = (m/pop) * n/(pop-1) * 0.5
nk = (n/pop) * k/(pop-1)
nm = (n/pop) * m/(pop-1) * 0.5

dom = round(kk + km + kn + mk + mm + mn + nk + nm, 5)
print(dom)
```
With this I finally got it right on my third attempt.

## PROT, Translating RNA into protein
We started this exercise in class and talked about breaking it down into smaller problems.
I decided to start with coding a for-loop that splits the string of RNA in triplets and saves it as a list, I iterated through the indices and only added 0 and the ones that can be devided by three and saved the letter ot that indice + the next two.
Next I saved the RNA-protein-pairs in a dictionary, I tried some ways to save me typing, but none was really that efficient...
Then I needed to write a new loop to translate the RNA to protein, but I had to be careful and include breaks at the stop codons!
This is my code:
```python
rna = ("AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA")
rna_split = []

#splits in pairs of 3 and saves to rna_split
for i in range(len(rna)):
    if i == 0:
        rna_split.append(rna[i:i+3])
    elif i % 3 == 0:
        rna_split.append(rna[i:i+3])
print(rna_split)

coding_dict = {
    'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 
    'GUU': 'V', 'UUC': 'F', 'CUC': 'L', 
    'AUC': 'I', 'GUC': 'V', 'UUA': 'L', 
    'CUA': 'L', 'AUA': 'I', 'GUA': 'V', 
    'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 
    'GUG': 'V', 'UCU': 'S', 'CCU': 'P', 
    'ACU': 'T', 'GCU': 'A', 'UCC': 'S', 
    'CCC': 'P', 'ACC': 'T', 'GCC': 'A', 
    'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 
    'GCA': 'A', 'UCG': 'S', 'CCG': 'P', 
    'ACG': 'T', 'GCG': 'A', 'UAU': 'Y', 
    'CAU': 'H', 'AAU': 'N', 'GAU': 'D', 
    'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 
    'GAC': 'D', 'UAA': 'Stop', 'CAA': 'Q', 
    'AAA': 'K', 'GAA': 'E', 'UAG': 'Stop', 
    'CAG': 'Q', 'AAG': 'K', 'GAG': 'E', 
    'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 
    'GGU': 'G', 'UGC': 'C', 'CGC': 'R', 
    'AGC': 'S', 'GGC': 'G', 'UGA': 'Stop', 
    'CGA': 'R', 'AGA': 'R', 'GGA': 'G', 
    'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 
    'GGG': 'G'}

protein = ""

for i in rna_split:
    if coding_dict[i] != "Stop":
        protein = protein + coding_dict[i]
    else:
        break

print(protein)
```
With this I solved it in my first attempt.

