#>Rosalind_0498
#AAATAAA
#>Rosalind_2391
#AAATTTT
#>Rosalind_2323
#TTTTCCC
#>Rosalind_0442
#AAATCCC
#>Rosalind_5013
#GGGTGGG

#Rosalind_0498 Rosalind_2391
#Rosalind_0498 Rosalind_0442
#Rosalind_2391 Rosalind_2323

rosalind_input = open("GRPH_input.txt", "r")
fasta_list = rosalind_input.read()
fasta_list = fasta_list.split(">")
fasta_list = fasta_list[1:]

fasta_dict = {}

for i in fasta_list:
    i = i.split("\n")
    key = i[0]
    value = ""
    for j in i[1:]:
        value = value + j
    fasta_dict[key] = value

#print(fasta_dict)

for fasta1, string1 in fasta_dict.items():
    for fasta2, string2 in fasta_dict.items():
        if string1 != string2:
            if string1[-3:] == string2[:3]:
                print(fasta1, fasta2)

#dna_strings = ["AAATAAA", "AAATTTT", "TTTTCCC", "AAATCCC", "GGGTGGG"]

#for string1 in dna_strings:
#    for string2 in dna_strings:
#        if string1 != string2:
#            if string1[-3:] == string2[:3]:
#                print(string1, string2)