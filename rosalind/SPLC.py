#cut out introns
#translate rest
#look up previous exercises

#find introns in gene
#def find_intron(gene, intron)
#1. go through gene in steps of 1
#2. look at an intron-sized window
#3. check if window == intron
    #if yes, return pos_start, intron_length + pos_start = pos_end
#def remove_intron(gene, pos_start, pos_end)
    #SLICING

input_splc = open("input_splc.txt", "r")
fasta_list = input_splc.read().split(">")[1:]

input_gene = fasta_list[0].split("\n")[1]
fasta_list = fasta_list[1:]
#print(input_gene)
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

def del_intron(gene, intron):
    for i in range(len(gene)):
        if gene[i:i+len(intron)] == intron:
            rna_split = gene[:i] + gene[i+len(intron):]
            return rna_split
        
#print(del_intron(gene, intron1))
        
for fasta_intron in fasta_dict.values():
    input_gene = del_intron(input_gene, fasta_intron)
    #print(input_gene)
#print(input_gene)

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

input_gene = input_gene.replace("T", "U")
#print(input_gene)

rna_split = []

for i in range(len(input_gene)):
    if i == 0:
        rna_split.append(input_gene[i:i+3])
    elif i % 3 == 0:
        rna_split.append(input_gene[i:i+3])
#print(rna_split)

protein = ""

for i in rna_split:
    if coding_dict[i] != "Stop":
        protein = protein + coding_dict[i]
    else:
        break

print(protein)