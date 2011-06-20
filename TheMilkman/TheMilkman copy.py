#!/usr/bin/python
import sys 
import itertools

"""
total_cows
cows
total_posibilities
weight_limit
cow_weight
cow_milk
"""

def generate_posibilities():
    #global total_cows, cows
    
    posibilities_buffer = [];
    
    for cow in cows:
        posibilities_buffer.append([cow])
    
        i = 0
        while i < total_cows-1:
            posibilities_buffer = generate_next_posibilities(posibilities_buffer)
            i += 1
        
        total_posibilities += posibilities_buffer


    total_posibilities = filter_posibilities_per_weight(total_posibilities)
    
    return total_posibilities


def generate_next_posibilities(posibilities_buffer):
    #global total_cows, cows;
    
    new_posibilities_buffer = []
    
    for posibilities in posibilities_buffer:
        for cow in cows:
            if cow not in posibilities:
                new_posibiliti = list(posibilities)
                new_posibiliti.append(cow)
                
                new_posibilities_buffer.append(new_posibiliti)
        
        posibilities_buffer.remove(posibilities)
        posibilities_buffer += new_posibilities_buffer

    return posibilities_buffer

def filter_posibilities_per_weight(total_posibilities):
    #global weight_limit, cow_weight
    
    for posibiliti in total_posibilities:
        weight = 0
        new_posibiliti = []
        
        for cow in posibiliti:
            if weight + cow_weight[cow] <= weight_limit:
                weight += cow_weight[cow]
                new_posibiliti += cow
        
        posibiliti = new_posibiliti
    
    return total_posibilities

def milk_per_posibilities(total_posibilities):
    #global cow_milk
    
    total_milk = []
    
    for posibiliti in total_posibilities:
        milk = 0;
        
        for cow in posibiliti:
            milk += cow_milk[cow]
        
        total_milk.append(milk)
    
    #total_milk = array_merge_recursive(array(), array_unique($total_milk));
    total_milk.sort(reverse=True)
    
    return total_milk

def maximized_milk_production(milk_per_posibilities):
    return milk_per_posibilities[0]
"""
#main
#for line in sys.stdin:
line = "7 7923 4,409,292,347,276,365,679 53,30,49,67,7,17,61"
line = line.strip().split(" ")
    
total_cows = int(line[0])
weight_limit = int(line[1])
cows = range(0, total_cows-1)
    
cow_weight = line[2].split(",")
cow_milk = line[3].split(",")
    
total_posibilities = generate_posibilities();
milk_per_posibilities = milk_per_posibilities(total_posibilities)
output = maximized_milk_production(milk_per_posibilities)
    
print output
"""
