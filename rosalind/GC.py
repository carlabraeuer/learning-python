rosalind_cg = open("rosalind_cg", "r")
fasta_list = rosalind_cg.read()
fasta_list = fasta_list.split(">")
fasta_list = fasta_list[1:]
#print(fasta_list)

fasta_dict = {}

for i in fasta_list:
    i = i.split("\n")
    key = i[0]
    value = ""
    for j in i[1:]:
        value = value + j
    fasta_dict[key] = value
#print(fasta_dict)

gc = []

for k in fasta_dict:
    g = fasta_dict[k].count("G")
    c = fasta_dict[k].count("C")
    length = len(fasta_dict[k])
    fasta_dict[k] = round((c+g) * 100 / length, 6)
    gc.append(fasta_dict[k])
#print(fasta_dict)

highest = max(gc)

for key in fasta_dict.keys():
    if fasta_dict[key] == highest:
        print(key)
        print(highest)