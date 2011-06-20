#!/usr/bin/python

# Task Duration
# @author Imanol Urra (index02@gmail.com)
#
# Years ago, my mother said to me: You are not less than anyone, then, if they can, you can too.
# - My Mom
#

# Imports
import sys

# Functions
def find_task(task_id):
    infile = open('in', 'r')
    
    match = []
    
    for line in infile.readlines():
        if line.startswith(task_id+","):
            line = line.strip().split(",")
            del line[0]
            match += [line]
        if len(match) == 2:
            break
    
           
    infile.close()
    
    return match

def calculate_time(tid):
    total_time = 0
    time = 0
    
    task = find_task(tid)
    
    if len(task) > 1:
        for did in task[1]:
            time += calculate_time(did)
            
            if time > total_time:
                total_time = time
            
            time = 0
            
    total_time += int(task[0][0])

    return total_time

# Main
for line in sys.stdin:
    line = line.strip().split(",")
    for tid in line:
        print tid +" "+ str(calculate_time(tid))