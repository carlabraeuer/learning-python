file = open("day1_input.txt", "r")
numbers = []
for line in file.readlines():
    
    #numbers_written = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]:

    line_copy = line
    for index in range(len(line)):
        if line[index:].startswith("one"):
            line_copy.replace("one", "1", 1)
            break
        if line[index:].startswith("two"):
            line_copy.replace("two", "2", 1)
            break
        if line[index:].startswith("three"):
            line_copy.replace("three", "3", 1)
            break
        if line[index:].startswith("four"):
            line_copy.replace("four", "4", 1)
            break
        if line[index:].startswith("five"):
            line_copy.replace("five", "5", 1)
            break
        if line[index:].startswith("six"):
            line_copy.replace("six", "6", 1)
            break
        if line[index:].startswith("seven"):
            line_copy.replace("seven", "7", 1)
            break
        if line[index:].startswith("eight"):
            line_copy.replace("eight", "8", 1)
            break
        if line[index:].startswith("nine"):
            line_copy.replace("nine", "9", 1)
            break

    line = line[::-1]
    line_copy = line
    for index in range(len(line)):
        if line[index:].startswith("one"[::-1]):
            line.replace("one"[::-1], "1", 1)
            break
        if line[index:].startswith("two"[::-1]):
            line.replace("two"[::-1], "2", 1)
            break
        if line[index:].startswith("three"[::-1]):
            line.replace("three"[::-1], "3", 1)
            break
        if line[index:].startswith("four"[::-1]):
            line.replace("four"[::-1], "4", 1)
            break
        if line[index:].startswith("five"[::-1]):
            line.replace("five"[::-1], "5", 1)
            break
        if line[index:].startswith("six"[::-1]):
            line.replace("six"[::-1], "6", 1)
            break
        if line[index:].startswith("seven"[::-1]):
            line.replace("seven"[::-1], "7", 1)
            break
        if line[index:].startswith("eight"[::-1]):
            line.replace("eight"[::-1], "8", 1)
            break
        if line[index:].startswith("nine"[::-1]):
            line.replace("nine"[::-1], "9", 1)
            break
    line = line[::-1]
        

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