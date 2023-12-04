#given: game file
#Return: sum game_ids where possible 12r 13g 14b

# possible: 12r = xt, 13g = yt, 14b = zt          t = true
# round1: xr yg zb 
# round2: x'r y'g z'b
# round3: ....
# x <= xt, y <= yt, z <= zt

#game_round(x, y, z, xt, yt, zt):
#if: (x <= xt) and (y <= yt) and (z <= zt)
    
# every round needs to be valid! then game is valid

#def game_round(x, y, z, xt, yt, zt):
    #if (x <= xt) and (y <= yt) and (z <= zt):
        #return True
    #else:
        #return False

#example1 : 
# Game 1: 
#   3 blue, 4 red; 
#   1 red, 2 green, 6 blue; 
#   2 green

#game_round(round1["red"], 
           #round1["green"], 
           #round1["blue"], 
           #maximum_values["red"], 
           #maximum_values["green"], 
           #maximum_values["blue"])

#round1 = {"blue" : 3, "red" : 4, "green" : 0}
#round2 = {"red" : 1, "green" : 2, "blue" : 6}
#round3 = {"green" : 2, "blue" : 0, "red" : 0}

# now for the input:
# : separates game ID from rounds
# ; separetes rounds within game
# , separetes coulours within round
file = open("day2_input.txt", "r")
all_games_dict = {}
for line in file.readlines():
    line = line.strip("\n")
    both = line.split(": ")
    rounds = both[1].split("; ")
    #print(rounds)
    this_game = []
    for i in rounds:
        one_round = i.split(", ")
        #print(one_round)
        one_round_dict = {}
        for j in one_round:
            one_colour = j.split(" ")
            #print(one_colour)
            one_round_dict[one_colour[1]] = int(one_colour[0])
        #print(one_round_dict)
        this_game.append(one_round_dict)
        #print(this_game)
    game_id = both[0]
    game_id = game_id[5:]
    #print(game_id)
    all_games_dict[game_id] = this_game

#print(all_games_dict)

maximum_values = {"red" : 12, "green" : 13, "blue" : 14}

def game_round(red, green, blue, red_total, greeen_total, blue_total):
    if (red <= red_total) and (green <= greeen_total) and (blue <= blue_total):
        return True
    else:
        return False
    
# game is list of rounds
#game1 = [round1, round2, round3]

#combining everything
def is_game_valid(game):
    is_valid = []
    for round in game:
        current_round = game_round(round["red"],
                                round["green"],
                                round["blue"],
                                maximum_values["red"],
                                maximum_values["green"],
                                maximum_values["blue"])
        is_valid.append(current_round)
    game_valid = all(is_valid)
    return game_valid
#print(is_game_valid(all_games_dict["98"]))
# ERROR: what if one round does not have all colours

#print(all_games_dict["100"])
#print(game1)

valid_games = []
#for game_id in all_games_dict.keys():
    #print(game_id)
    #if is_game_valid == True:
        #valid_games.append("game_id")

#print(valid_games)
