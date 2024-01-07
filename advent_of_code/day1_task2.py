#with the help of sophias and monikas solution, I could get around the edgecases :)

file = open("day1_input.txt", "r")


lines = file.read()

word_to_number = {'oneight':'18', 'threeight':'38', 'fiveight':'58',
                  'nineight':'98', 'eightwo':'82', 'eighthree':'83',
                  'sevenine':'79','twone':'21', 
                  'one':'1', 'two':'2', 'three':'3',
                  'four':'4', 'five':'5', 'six':'6', 'seven':'7',
                  'eight':'8', 'nine':'9'}

for written, digit in word_to_number.items():
    lines = lines.replace(written, digit)
#print(lines)

numbers = []
for line in lines.split():
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