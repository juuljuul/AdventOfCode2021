import numpy as np
import re
import math

input = open("input_ex", "r")

result = 0
n_line = 0

#def depth(l):
#    if isinstance(l, list):
#        return 1 + max(depth(item) for item in l)
#    else:
#        return 0

for line in input:
    n_line += 1
    line = line.rstrip()
    new_array = line
    print(new_array)
    



    if n_line == 1:
        old_array = new_array
    else: #add two lines together
        array = old_array + "," + new_array
        depth = 0
        max_depth = 0
        numbers = []
        numbers_depth = []

        test = array.split(",")
        print("test:", test)
        for element in test:
            for character in element:
                if character == "[":
                    depth += 1
                elif character == "]":
                    depth -= 1
                elif character in ['0','1','2','3','4','5','6','7','8','9']:
                    #print("character is no bracket but ", character)
                    number = re.sub('\[|\]', '', element)
                    numbers.append(int(number))
                    numbers_depth.append(depth)
                    print("number is: ", number)
                else:
                    pass
                    #print("character is none of the above but ", character)
                if depth > max_depth:
                    max_depth = depth
                if depth < 0:
                    raise ValueError("depth of vector is <0??")
        print(numbers)
        while max_depth >= 4 or any(x>=10 for x in numbers):
            if max_depth >= 4:
                # let pair explode
                print("explode!")
                index = numbers_depth.index(max_depth)
                if index > 0:
                    numbers[index-1] = numbers[index-1] + numbers[index]
                if index < len(numbers)-2:
                    numbers[index+2] = numbers[index+2] + numbers[index+1]
                numbers[index+1] = 0
                numbers_depth[index+1] -= 1
                #print("numbers before: ", numbers)
                del numbers[index]
                del numbers_depth[index]
                #print("numbers after deleting index ", index, " : ", numbers)
                max_depth = max(numbers_depth)
                print(numbers)
                print(numbers_depth)
            else: #anynumbers>=10
                print("split!")
                index = numbers_depth.index(max_depth)
                indices = [x for x in numbers if x >= 10]
                print("indices: ", indices)
                index = numbers.index(indices[0])
                print("index: ", index)
                numbers.insert(index+1, math.ceil(numbers[index]/2))
                numbers_depth.insert(index+1, numbers_depth[index]+1)
                numbers[index] = math.floor(numbers[index]/2)
                numbers_depth[index] += 1
                max_depth = max(numbers_depth)
                print(numbers)
                print(numbers_depth)
        numbers_old = numbers
        numbers_depth_old = numbers_depth
                
    if n_line == 100: # file has 100 lines
        # calculate value
        print("end of file")

