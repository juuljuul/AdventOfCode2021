import numpy as np
import re

input = open("input", "r")
result = 0

for line in input:
    splitted = line.split("|")
    elements = re.split(" |\n", splitted[1])
    for x in elements:
        
        if (len(x)) == 2 or (len(x)) == 3 or (len(x)) == 4 or (len(x)) == 7:
            result+=1      

'''
6 segments: 0, 6, 9
2 segments: 1
5 segments: 2,3, 5
4 segments: 4
3 segmetns: 7
8 segments: 8
'''

print(result)