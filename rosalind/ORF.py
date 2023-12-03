#all possible ORF
#all possible ORF on both strands
#all possible ORF on both strands on all possible reading frames (RFs)
#ORF = ATG -> stop

#1. get DNA string + get reverse complement DNA string
#2. get 3 reading frames
#3. get all ATG in one of the six options

#Test
#ATGACCCCGCGACTTTAAGGATTAG
#option command F - find and replace
#command shift P - dictionary 

coding_dict = {
    "TTT": "F", "CTT": "L", "ATT": "I", 
    "GTT": "V", "TTC": "F", "CTC": "L", 
    "ATC": "I", "GTC": "V", "TTA": "L", 
    "CTA": "L", "ATA": "I", "GTA": "V", 
    "TTG": "L", "CTG": "L", "ATG": "M", 
    "GTG": "V", "TCT": "S", "CCT": "P", 
    "ACT": "T", "GCT": "A", "TCC": "S", 
    "CCC": "P", "ACC": "T", "GCC": "A", 
    "TCA": "S", "CCA": "P", "ACA": "T", 
    "GCA": "A", "TCG": "S", "CCG": "P", 
    "ACG": "T", "GCG": "A", "TAT": "Y", 
    "CAT": "H", "AAT": "N", "GAT": "D", 
    "TAC": "Y", "CAC": "H", "AAC": "N", 
    "GAC": "D", "TAA": "Stop", "CAA": "Q", 
    "AAA": "K", "GAA": "E", "TAG": "Stop", 
    "CAG": "Q", "AAG": "K", "GAG": "E", 
    "TGT": "C", "CGT": "R", "AGT": "S", 
    "GGT": "G", "TGC": "C", "CGC": "R", 
    "AGC": "S", "GGC": "G", "TGA": "Stop", 
    "CGA": "R", "AGA": "R", "GGA": "G", 
    "TGG": "W", "CGG": "R", "AGG": "R", 
    "GGG": "G"}

dna = ("CATTGGATGATCAAACAACGGGAGTCCATCACAAAGCACTATTCGAACCGTCTTTCTGCACCCCCGGGATTCCTTAATAACTAAAGGCACATACTCCGGAGCCGTACTTGGTTGCACAACCAGAGGTAATCCCAGGAAAAGTTACAAATCTCATAGTTTAAACGAGGCGCCTCACATGCTTCCTGCCGAACAGTGTCAGCAACATGCAAGGCATCTGTCTGCGTCGTCCTTTTTCGACATACAGACACTCGCAGATCATTAGGCACGGAGAAATGCCTTTAACTAGATGGATATCAGTATAGCATAGCAGCTTGCTCTAGTTATGATGGTGTGCGATCGATTCGATGATAAGAAGTAGTACTCCCAATCTTGACTTGAAAACGGGCCGCTCAGGCTTTGGTTATGAAAATTTTATAACCCATCTGTGCTAACACGCTTGCGAAATGCATGGTAGCTCTTACTCGACTAACCTGTAGCTACAGGTTAGTCGAGTAAGAGCTACCATGCATTTAACTTCAAGTTACGTGCGCACTCGGAGGGCTAGTTAACGCTTTTCCCATGGAGATTAATAGACCTATGTAGGCTAAACTTTATATCTGCAATGGCAAGAATGATATCGGGGTACGGCTGATTTGATTTTTGAGCAGACCTATTGTCTCTGAACCGACGTTCTGCACAGTATGATTGCAGAGGATACTTCACCTCGAGGGTATAACTTAAGTTCCTGTTCGGGTTCCTATTCGGAAATACTTTTTGACGTCTACGTCCGCATCAGGATAGACTGTAAATCATTCCCCCGCTCACGCACATAGCAGCCAGCGTTGTGTCACCTTCTTTTTCCGCAGAAAGGGGTCCCAATGCCGACGCAATTAGTTCAAGGGTTAGGAACACCAGAACAACAGATATCTTTTTGTACGGAATGGCCGTATTAAATTCGAACTGGGAGAAGAAT")
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
#print(reverse)

frame_1 = dna
frame_2 = dna[1:]
frame_3 = dna[2:]
frame_4 = reverse
frame_5 = reverse[1:]
frame_6 = reverse[2:]

all_frames = [frame_1, frame_2, frame_3, frame_4, frame_5, frame_6,]
all_frames_split = []

for frame in all_frames:
    split = []
    for i in range(len(frame)):
        if i == 0:
            split.append(frame[i:i+3])
        elif i % 3 == 0:
            split.append(frame[i:i+3])
    #print(split)
    all_frames_split.append(split)
#print(all_frames_split)

#dna_split = ['ATG', 'ACC', 'ATG', 'CCG', 'CGA', 'CTT', 'TAA', 'GGA', 'TTA', 'G']

protein_list = []

for list in all_frames_split:
    while list.count("ATG") > 0:
        start = ""
        stop = ""
        index = 0
        for triplet in list:
            if triplet == "ATG" and start == "":
                start = index
            if start != "" and (triplet == "TAA" or triplet == "TAG" or triplet == "TGA"):
                stop = index
                break
            index = index + 1
        #print(start, stop)
        to_translate_all = []
        protein = ""
        if start != "" and stop != "":
            to_translate = list[start:stop]
            #print(to_translate)
            for codon in to_translate:
                if coding_dict[codon] != "Stop":
                    protein = protein + coding_dict[codon]
                else:
                    break
            protein_list.append(protein)
            #print(protein)
        list.remove("ATG");

distinct = []
for case in protein_list:
    if case not in distinct:
        distinct.append(case)
        print(case)