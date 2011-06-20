#!/usr/bin/python

import sys
import re
for line in sys.stdin:
    add = 0
    for number in re.findall('3(,.+)', line):
        add += int(number)
    
    print add