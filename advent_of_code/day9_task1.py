file = open("day9_input.txt", "r")
lines = file.read()

lines = lines.split("\n")

def all_zero(list):
    for n in list:
        if n != 0:
            return False
    return True

def add_next(list):
    pd = []
    for i in range(len(list)):
        if i < len(list) -1:
            pd.append(list[i+1] - list[i])
    if all_zero(pd):
        return 0
    else:
        return pd[-1] + add_next(pd)

def predict_next(list):
    return list[-1] + add_next(list)

sum = 0  
for line in lines:
    lines_list = line.split(" ")
    for i in range(len(lines_list)):
        lines_list[i] = int(lines_list[i])
    number = predict_next(lines_list)
    sum = sum + number

print(sum)