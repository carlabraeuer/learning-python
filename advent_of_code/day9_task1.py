#find the next number of all sequences
#add next numbers

#GIVEN: lists of numbers - sequence has a pattern

list_one = [1, 3, 6, 10, 15, 21]

def all_zero(num):
    # if list empty, reurn false
    if len(num) == 0:
        return False
    for n in num:
        if n != 0:
            return False
    return True

import copy

def predict_next(input_list):
    last_pos = []
    last_pos.append(input_list[-1])
    #print(last_pos)
    try_list = copy.deepcopy(input_list)
    diff_list  = []
    while not all_zero(diff_list):
        for i in range(len(try_list)):
            if i + 1 < len(try_list):
                diff_list.append(try_list[i + 1] - try_list[i])
            print(diff_list)
        try_list = diff_list
        last_pos.append(diff_list[-1])
        print(diff_list)
    return(last_pos)

predict_next(list_one)

# boolean values all-function to check for 0!!!!! 
