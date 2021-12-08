import numpy as np
import re
from itertools import permutations

input = open("input", "r")
result = 0

for line in input:
    splitted = line.split("|")
    allelements = re.split(" |\n|\|", line)
    array = ['']*10 # tell us which number corresponds to which letters
    singles = ['']*8 # tells us which letter is on which position, reading the 7 display from left to right, bottom to top
    one = ['', '']
    seven = ['', '', '']
    four = ['', '', '', '']

    for x in allelements:
        if len(x) == 2:
            one[0] = x[0]
            one[1] = x[1]
            array[1] = x
        elif len(x) == 3:
            seven[0] = x[0]
            seven[1] = x[1]
            seven[2] = x[2]
            array[7] = x
        elif len(x) == 4:
            four[0] = x[0]
            four[1] = x[1]
            four[2] = x[2]
            four[3] = x[3]
            array[4] = x
        elif len(x) == 7:
            singles[1] = x[0]
            singles[2] = x[1]
            singles[3] = x[2]
            singles[4] = x[3]
            singles[5] = x[4]
            singles[6] = x[5]
            singles[7] = x[6]
            array[8] = x

    #define numbers
    # 5 is singles at 7,1,4,6,2 (all except 3,5) not 1,7
    # 2 is singles at 5,7,1,4,3 (all except 2,6) not 4
    # 3 is singles at 4,6,7,3,1 (all except 2,5) not 1,4
    # 9 is singles at all except 5 not 1
    # 6 is singles at all except 2 not 4
    # 0 is singles at all except 4

    # find elements that are in 4 but not in 1
    # twice since sometimes only one is removed
    for i in four:
        if i == one[0] or i == one[1]:
            four.remove(i)
    for i in four:
        if i == one[0] or i == one[1]:
            four.remove(i)

    for x in allelements:
        if len(x) == 6:
            # zero is the only of length 6 where the middle wire is not illuminated
            # (which is in 4 but not in 1)
            if four[0] not in x or four[1] not in x:
                array[0] = x
            # 9 is the only other of length 6 where both elements of 1 is included
            elif one[0] in x and one[1] in x:
                array[9] = x
            # 6 is left over
            else:
                array[6] = x
        if len(x) == 5:
            # 5 is the only of length 5 where both of 4\1 is included
            if four[0] in x and four[1] in x:
                array[5] = x
            # 3 is the only of length 5 where both of 1 are also illuminated
            elif one[0] in x and one[1] in x:
                array[3] = x
            # 2 is left over
            else:
                array[2] = x
        
    # sort by alphabet since the characters are shuffeled
    a_string = "".join(sorted(array[2]))

    # sort all characters by alphabet
    for i in range(len(array)):
        array[i] = "".join(sorted(array[i]))
    
    elements2 = re.split(" |\n", splitted[1])
    # decode 
    sol = []
    for element in elements2:
        element = "".join(sorted(element))
        if element != '':
            sol.append(array.index(element))
    result += 1000*sol[0] + 100 * sol[1] + 10*sol[2] + sol[3]

'''
6 segments: 0, 6, 9
2 segments: 1
5 segments: 2,3, 5
4 segments: 4
3 segmetns: 7
8 segments: 8
'''

print("result: ", result)