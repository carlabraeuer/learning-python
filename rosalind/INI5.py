f = open("rosalind_ini5.txt", "r")
data = f.readlines()
i = 0
for line in data:
    if i % 2 == 1:
        print(line.strip())
    i = i + 1