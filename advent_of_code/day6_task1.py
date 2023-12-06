# GIVEN: we are given a list of times and a list of distances
# WANT: product of number of ways we can beat all records
# 4 subproblems:
# 1. beat the record
# 2. how many ways to beat the record
# 3. do it for all of them
# 4. multiplicate all the ways

# 4. 
# w1 * w2 * w3 * w4
# [w1, w2, w3, w4] = ways
# product = 1
# for numbers in ways:
#   product = product * number

# 3. "keyword all is a hint for a loop" all races -> [for]

# 1. 
# first race: 7ms 9mm
# we press a button to increase speed - then speed will be constant
# *picture*
# GIVEN: record = 9, race_time = 7
# dist_travel > record
# bpt = button-press-time, tt = travel-time
# bpt + tt = race_time
# tt = race_time - bpt
# speed = bpt
# distance = travel_time * speed
# for bpt in range(race_time):
#       tt = ...
#       speed = ...
#       dist = ...

#Time:      7  15   30
#Distance:  9  40  200

#Time:        62     73     75     65
#Distance:   644   1023   1240   1023

#race_times_records_dict = {9 : 7, 40 : 15, 200 : 30}
#race_times_records_dict = {644 : 62, 1023 : 73, 1240 : 75, 1023 : 65}
race_time_input = []
records_input = []

input = open("day6_input.txt", "r")
for line in input.readlines():
    line = line.strip("\n")
    if line.startswith("Time"):
        race_time_input.append(line)
    else:
        records_input.append(line)

race_time_input = race_time_input[0]
race_time_input = race_time_input.split(":")
race_time_input = race_time_input[1]
race_time_input = race_time_input.split(" ")
race_time_input = [item for item in race_time_input if item != '']

records_input = records_input[0]
records_input = records_input.split(":")
records_input = records_input[1]
records_input = records_input.split(" ")
records_input = [item for item in records_input if item != '']

#print(race_time_input, records_input)

race_times_records_dict = {}
for items in range(len(race_time_input)):
    race_times_records_dict[int(race_time_input[items])] = int(records_input[items])
#print(race_times_records_dict)

ways = []

for race_time, record in race_times_records_dict.items():
    #print(record)
    #print(race_time)
    distances = []
    for bpt in range(race_time):
        distance = bpt * (race_time - bpt)
        if distance > record:
            distances.append(distance)
        #print(distances)
        number_of_ways = 0
        for way in distances:
            number_of_ways = number_of_ways + 1
            #print(number_of_ways)
    ways.append(number_of_ways)
#print(ways)

product = 1
for numbers in ways:
    product = product * numbers

print(product)
