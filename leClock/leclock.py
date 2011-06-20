#!/usr/bin/python

# Le clock
# @author Imanol Urra (index02@gmail.com)
#
# The early bird gets the worm.
# - another typical proverb
#

#Imports
import sys

#Globals
leds_on_per_digit = (6, 2, 5, 5, 4, 5, 6, 3, 8, 5)

#Functions
# calcula_sum_on_led: calculate de sum of switched on leds
def calcula_sum_on_led(le_clock):
    global leds_on_per_digit
    
    total_led_on = 0
    for digit in le_clock:
        total_led_on += leds_on_per_digit[int(digit)]
    
    return total_led_on

# init_le_clock: calculate al switched on segment from 00:00:00 until expecified second
def init_le_clock(secs):
    le_clock = [0, 0, 0, 0, 0, 0]
    total_leds_on_sum = 0
    
    for sec in range(0, secs+1):
        h = '%02d' % (sec/3600)
        m = '%02d' % ((sec%3600)/60)
        s = '%02d' % (sec%60)
        
        le_clock[0] = h[0]
        le_clock[1] = h[1]
        le_clock[2] = m[0]
        le_clock[3] = m[1]
        le_clock[4] = s[0]
        le_clock[5] = s[1]
        
        total_leds_on_sum += calcula_sum_on_led(le_clock)
    
    return total_leds_on_sum

#main
for line in sys.stdin:
    secs = int(line)
    print init_le_clock(secs)