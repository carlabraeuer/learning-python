# now for the input:
# : separates game ID from rounds
# ; separetes rounds within game
# , separetes colours within round

#round1 = {"blue" : 3, "red" : 4, "green" : 0}
#round2 = {"red" : 1, "green" : 2, "blue" : 6}
#round3 = {"green" : 2, "blue" : 0, "red" : 0}

#game1 = [round1, round2, round3]
#all games = {1 : game1}

file = open("day2_input.txt", "r")
all_games_dict = {}
for line in file.readlines():
    line = line.strip("\n")
    both = line.split(": ")
    rounds = both[1].split("; ")
    #print(rounds)
    game = []
    for i in rounds:
        one_round = i.split(", ")
        #print(one_round)
        one_round_dict = {}
        for j in one_round:
            one_colour = j.split(" ")
            #print(one_colour)
            one_round_dict[one_colour[1]] = int(one_colour[0])
        #print(one_round_dict)
        game.append(one_round_dict)
        #print(game)
    game_id = both[0]
    game_id = game_id[5:]
    #print(game_id)
    all_games_dict[game_id] = game

print(all_games_dict)
