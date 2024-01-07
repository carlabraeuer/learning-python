file = open("day4_input.txt", "r")
lines = file.read()

lines = lines.split("\n")

lines_length = len(lines)
card_dict = {}

for line in range(1, lines_length +1):
    card_dict[line] = 1

for line in lines:
    wins = 0
    s = line.split(":")

    current_card = s[0].split(" ")
    current_card = current_card[-1]

    s = s[1].split("|")
    win_numbers = s[0].split(" ")
    my_numbers = s[1].split(" ")
    # print(win_numbers, my_numbers)

    for winning_number in win_numbers:
        if winning_number in my_numbers and winning_number != "":
            wins = wins + 1  

    if wins > 0:
        for i in range(1, card_dict[int(current_card)] +1):
            for j in range(1, wins +1):
                card_dict[int(current_card) + j] = card_dict[int(current_card) + j] + 1

sum = 0
for i in range(1, lines_length +1):
    sum = sum + card_dict[i]

print(sum)