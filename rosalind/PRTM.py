str_to_weight_dict = {
"A": 71.03711,
"C": 103.0091,
"D": 115.0269,
"E": 129.0425,
"F": 147.0684,
"G": 57.02146,
"H": 137.0589,
"I": 113.0840,
"K": 128.0949,
"L": 113.0840,
"M": 131.0404,
"N": 114.0429,
"P": 97.05276,
"Q": 128.0585,
"R": 156.1011,
"S": 87.03203,
"T": 101.0476,
"V": 99.06841,
"W": 186.0793,
"Y": 163.0633, }

weight = []
protein = "DADNAVVWPDSVIPMSDRWLTCVTWNTLPTDARCQDHMKYTQSADLRPPECGNSGTEIWEPMGAVRKPVVYALPWPQDTMDMIWTDKNSRGLRIGLSSDTGKMTVIKNSYAHPGPISWLKQMWHDIICAAHIRSHMGTNLETICMIVRNCQTDSMAGAARSKVSQCLEHLNHQKLVEISTMPRVDSKDCQYGALELGSEETDLNNYVIQHGCANYRIVMQAQHKCETHDPSYPRCYEQPLKEEKPTASQYSACGFELFTIHHKNPIDGFQEKALPFIIWQINANFACQPVSRHMLKVHGCHICQCTRHGCLNCAWTMDLQMQHQNGWAQCSDSWDSMLWKWNDFVVWIMRPWMALNDFAPNCAICHNIRIITIYKALFFDFHGKEWWQDMMGVHSFSETDCEEQWWCDWQEFAFTFSPEIMKHCWWGYVIRGGFMSDPGLCPSRKQYEYARAASCISCYSIWRNQLDIEYLPAKCPQADKVWGKKMPPACDDPCAKVQVHTTGFYYWVQWYELVFLHQKLVMELTGHHEINNAPIWHAKSGYIYLCMRGTNKDNFEWCRCPLVCGSLQYMFARCGCVCALHHCNVPTFDQTKDHHHWGLEGRLHRRKCQDARICVMWYPNYVMEYEDEWSRKPHHKHTNYHDANWIIISPWFMICVDIHITFVFCSFDETTEYSIQFHFMYLIKFINIFALNVTPMCLNDVQADFDRGCYGFTSSHGGCSKQALDEHASCWYKNAQDLIVNHKFTIQGEWAFKFPIVSYKRWDVFVAHGRTYEPFYLLPCYAVTQEKNFDAGEFWRHTVNFGGMVCQGIHVQMKQSRTRVRLKQGLDRNVAKGPKSSDMWCLKQALKDHHREWQSRHRKMVFDEPVNACFKMRMLIIAYMKNRILMLPIHPCKDCYHLTQLIEMEEQCVQCVHPEKSRINNNKIWTYPPPPSDHISPSLFIQANEDWSFTIEHHDVLIGCELDLQAYMNRIK"

for symbol in protein:
    weight.append(str_to_weight_dict[symbol])

print(sum(weight))