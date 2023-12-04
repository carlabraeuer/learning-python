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
all_game = []
for line in file.readlines():
    line = line.strip("\n")
    both = line.split(": ")
    rounds = both[1].split("; ")
    #print(rounds)
    one_game_dict = {"red" : 0, "green" : 0, "blue" : 0}
    for i in rounds:
        one_round = i.split(", ")
        #print(one_round)
        for j in one_round:
            one_colour = j.split(" ")
            #print(one_colour)
            if int(one_colour[0]) > one_game_dict[one_colour[1]]:
                one_game_dict[one_colour[1]] = int(one_colour[0])
            power_min = one_game_dict["red"] * one_game_dict["green"] * one_game_dict["blue"]
    all_game.append(power_min)
    print(one_game_dict)
    print(power_min)
print(all_game)
print(sum(all_game))
    #all_game.append(one_round_dict)
    #print(all_game)

    #game_id = both[0]
    #game_id = game_id[5:]
    #print(game_id)
    #all_games_dict[game_id] = this_game

