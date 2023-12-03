file = open("day1_input.txt", "r")
numbers = []
for line in file.readlines():
    first = ""
    last = ""
    for char in line:
        if char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            first = char
            break
    for char in line[::-1]:
        if char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            last = char
            break
    #print(line)
    both = first + last
    if both != "":
        #print(both)
        numbers.append(int(both))

print(sum(numbers))