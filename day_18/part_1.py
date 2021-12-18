import numpy as np
import re
import math

input = open("input", "r")

result = 0
n_line = 0

for line in input:
    n_line += 1
    line = line.rstrip()

    depth = 0
    numbers_new = []
    numbers_depth_new = []

    test = line.split(",")
    #print("test:", test)
    for element in test:
        for character in element:
            if character == "[":
                depth += 1
            elif character == "]":
                depth -= 1
            elif character in ['0','1','2','3','4','5','6','7','8','9']:
                number = re.sub('\[|\]', '', element)
                numbers_new.append(int(number))
                numbers_depth_new.append(depth)
            else:
                pass
            if depth < 0:
                raise ValueError("depth of vector is <0??")

    if n_line == 1:
        numbers_old = numbers_new
        numbers_depth_old = numbers_depth_new
    else: #add two lines together
        numbers = numbers_old + numbers_new
        numbers_depth = numbers_depth_old + numbers_depth_new
        numbers_depth = [x+1 for x in numbers_depth]
        max_depth = max(numbers_depth)
        #print(numbers)
        #print(numbers_depth)
        while max_depth > 4 or any(x>=10 for x in numbers):
            if max_depth > 4:
                # let pair explode
                #print("explode!")
                index = numbers_depth.index(max_depth)
                if index > 0:
                    numbers[index-1] = numbers[index-1] + numbers[index]
                if index < len(numbers)-2:
                    numbers[index+2] = numbers[index+2] + numbers[index+1]
                numbers[index+1] = 0
                numbers_depth[index+1] -= 1
                del numbers[index]
                del numbers_depth[index]
                max_depth = max(numbers_depth)
                #print(numbers)
                #print(numbers_depth)
            else: #anynumbers>=10
                #print("split!")
                index = numbers_depth.index(max_depth)
                indices = [x for x in numbers if x >= 10]
                index = numbers.index(indices[0])
                numbers.insert(index+1, math.ceil(numbers[index]/2))
                numbers_depth.insert(index+1, numbers_depth[index]+1)
                numbers[index] = math.floor(numbers[index]/2)
                numbers_depth[index] += 1
                max_depth = max(numbers_depth)
                #print("numbers: ", numbers)
                #print("numbers_depth: ", numbers_depth)
        numbers_old = numbers
        numbers_depth_old = numbers_depth
        #print(numbers)
    
    if n_line == 100: # file has 100 lines
        print("end of file")
        # calculate result
        result = numbers.copy()
        print(type(result))
        while len(result)>1:
            new_array = []
            for i in range(0,len(result),2):
                a = 3*result[i] + 2*result[i+1]
                new_array.append(a)
            result = new_array
            print(len(result))

print("result: ", result)  
