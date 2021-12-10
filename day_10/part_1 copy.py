##################################
# first try, ended in a deadlock #
##################################

import numpy as np

input = open("input_ex", "r")

result = 0
n = 0

for line in input:
    print(n)
    array = np.zeros(4)
    last = []
    for character in line:
        if character == "(":
            array[0]+=1
        elif character == "[":
            array[1]+=1
        elif character == "{":
            array[2]+=1
        elif character == "<":
            array[3]+=1
        elif character == ")":
            array[0]-=1
        elif character == "]":
            array[1]-=1
        elif character == "}":
            array[2]-=1
        elif character == ">":
            array[3]-=1
        print(array)
        if any(x <0 for x in array):
            print("yess")
            if character == ")":
                result += 3
            elif character == "]":
                result += 57
            elif character == "}":
                result += 1197
            elif character == ">":
                result += 25137
            break
    else:
        pass
    n += 1
print(result)

input.close()
