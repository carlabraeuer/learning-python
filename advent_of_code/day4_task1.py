file = open("day4_input.txt", "r")
lines = file.read()

lines = lines.split("\n")

line_sum = []
for line in lines:
    wins = 0
    s = line.split(":")
    s = s[1].split("|")
    win_numbers = s[0].split(" ")
    my_numbers = s[1].split(" ")

    # print(win_numbers, my_numbers)

    for winning_number in win_numbers:
        if winning_number in my_numbers and winning_number != "":
            wins = wins + 1  

    if wins > 0:
        line_sum.append(2**(wins - 1))

print(sum(line_sum))