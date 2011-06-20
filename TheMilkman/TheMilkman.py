#!/usr/bin/python

# The Milkman problem
# @author Imanol Urra (index02@gmail.com)
#
# Third time's a charm. (x1000)
# - traditional and typical proverb
#

#Imports
import sys 
import itertools

#Functions

# find_possibilities: find and filter possibilities step by step
#  return: next filtered possibilities
def find_possibilities(start_possibilities_group):
    end_possibilities_group = []
    
    for possibility in start_possibilities_group:
        weight = 0
        possibility = list(possibility)
        cows_copy = list(cows)
        
        for cow in possibility:
            cows_copy.remove(cow)
        
        next_combinations = list(itertools.combinations(cows_copy, 2))
        for next in next_combinations:
            new_possibility = list(possibility)
            new_possibility += next
        
        new_combination = []
        for cow in new_possibility:
            if int(cow_weight[cow]) + weight <= weight_limit:
                weight += int(cow_weight[cow])
                new_combination.append(cow)
            
        end_possibilities_group.append(new_combination)
        
    return end_possibilities_group

# milk_per_possibilities: calculate milk productions from all possibilities
#  return: a list with milk productions for each possibilities
def milk_per_possibilities(total_possibilities):
    milk_per_possibility = []
    
    for possibility in total_possibilities:
        milk = 0
        
        for cow in possibility:
            milk += int(cow_milk[cow])
            
        milk_per_possibility.append(milk)
        
    milk_per_possibility.sort(reverse=True)
    return milk_per_possibility

# return_max_milk_production
#  return: max milk production
def return_max_milk_production(milk_per_possibility):
    return milk_per_possibility[0]
        
#main
for line in sys.stdin:
    line = line.strip().split(" ")
    
    total_cows = int(line[0])
    weight_limit = int(line[1])
    cows = range(0, total_cows)
    
    cow_weight = line[2].split(",")
    total_cow_weight = 0;
    cow_milk = line[3].split(",")
    
    for weight in cow_weight:
        total_cow_weight += int(weight)

    if total_cow_weight <= weight_limit:
        possibilities = [cows]
    
    else:
        i = 0
        i_max = total_cows/2-2
        r = 2
        
        if total_cows % 2 != 0: 
            r = 3
            i_max = (total_cows-3)/2-1
    
        possibilities = find_possibilities(list(itertools.combinations(cows, r)))

        while i < i_max:
            possibilities = find_possibilities(possibilities)
            i += 1


    milk_list = milk_per_possibilities(possibilities)
    result = return_max_milk_production(milk_list)

    print result