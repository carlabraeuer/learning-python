#we need to define the tiles of the map
#first lines = rows, then positions = colums

#sketch[0][2]

#GIVEN: map, navigation instructions, Flobby starting point (FSP)
#WANTED: loop through FSP (FSPL), furthest pos. on FSPL

# S = starting point
# | = connecting north and south
# - = connecting east and west
# L = connecting north and east
# J = connecting north and west
# 7 = connecting south and west
# F = connecting south and east
# . = ground

#  0 1 2 3 4 
#0 . . . . .
#1 . F - 7 .
#2 . S . | .
#3 . L - J .
#4 . . . . .

#previous pos. + navigation -> next pos.

#x, y

# | = can come from north OR south, x+1,y OR x-1,y
# - = can come from west  OR east,  x,y+1 OR x,y-1
# L = can come from north OR east,  x,y+1 OR x-1,y
# J = can come from north OR west,  x,y-1 OR x-1,y
# 7 = can come from south OR west,  x,y-1 OR x+1,y
# F = can come from south OR east,  x,y+1 OR x+1,y

#next_pos(prev_x, prev_y, current_x, current_y, current_symbol):
#   
#return next_x, next_y


def next_pos(prev_x, prev_y, current_x, current_y, current_symbol):
    if current_symbol == "|":
        if current_x > prev_x and current_y == prev_y:
            next_x = current_x + 1
            next_y = current_y
        elif current_x < prev_x and current_y == prev_y:
            next_x = current_x - 1
            next_y = current_y
    elif current_symbol == "-":
        if current_x == prev_x and current_y > prev_y:
            next_x = current_x
            next_y = current_y + 1
        elif current_x == prev_x and current_y < prev_y:
            next_x = current_x
            next_y = current_y - 1
    elif current_symbol == "L":
        if current_x > prev_x and current_y == prev_y:
            next_x = current_x
            next_y = current_y + 1
        elif current_x == prev_x and current_y < prev_y:
            next_x = current_x - 1
            next_y = current_y
    elif current_symbol == "J":
        if current_x > prev_x and current_y == prev_y:
            next_x = current_x
            next_y = current_y - 1
        elif current_x == prev_x and current_y > prev_y:
            next_x = current_x - 1
            next_y = current_y
    elif current_symbol == "7":
        if current_x < prev_x and current_y == prev_y:
            next_x = current_x
            next_y = current_y - 1
        elif current_x == prev_x and current_y > prev_y:
            next_x = current_x + 1
            next_y = current_y
    elif current_symbol == "F":
        if current_x < prev_x and current_y == prev_y:
            next_x = current_x
            next_y = current_y + 1
        elif current_x == prev_x and current_y < prev_y:
            next_x = current_x + 1
            next_y = current_y
    return(next_x, next_y)

#go to S  and find pipes going into it

#maybe find S and go though the loop till you're at S again
#append all to a list? 
#take length of appended list - use middle value or two if it's a "gerade zahl" 