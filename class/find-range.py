def find_within_range(list_of_numbers, lower=0, upper=10):
    output = []
    for number in list_of_numbers:
        if lower <= number <= upper:
            if number not in output:
                output.append(number)    
    return output

print(find_within_range([-2, 14, 9, 3.14]))              
print([9, 3.14])
print("==============================================================")
print(find_within_range([0, 5, 10, 15]))                 
print([0, 5, 10])
print("==============================================================")
print(find_within_range([2.104, 10000, -435, 2.104]))    
print([2.104])
print("==============================================================")
print(find_within_range([1, 2, 3, 4], lower=2, upper=6)) 
print([2, 3, 4])