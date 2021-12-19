import numpy as np
import re
import math

input = open("input", "r")

result = 0
n_line = 0
all_results = []

all_numbers = []
all_numbers_depth = []

for line in input:
    n_line += 1
    line = line.rstrip()

    depth = 0
    numbers_new = []
    numbers_depth_new = []

    test = line.split(",")
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
            if depth < 0:
                raise ValueError("depth of vector is <0??")
    all_numbers.append(numbers_new)
    all_numbers_depth.append(numbers_depth_new)

# add two lines together
for i in range(0,len(all_numbers)):
    for j in range(0,len(all_numbers)):
        if i != j:
            numbers = all_numbers[i] + all_numbers[j]
            numbers_depth = all_numbers_depth[i] + all_numbers_depth[j]
            numbers_depth = [x+1 for x in numbers_depth]
            max_depth = max(numbers_depth)
            while max_depth > 4 or any(x>=10 for x in numbers):
                if max_depth > 4:    # let pair explode
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

            result = numbers.copy()
            result_depth = numbers_depth.copy()
            max_depth = max(numbers_depth)
            while len(result)>1:
                new_array = []
                new_depth_array = []
                known = False
                for k in range(0,len(result)-1):
                    if known == False:
                        if result_depth[k] == max_depth:
                            a = 3*result[k] + 2*result[k+1]
                            #print(a)
                            new_array.append(a)
                            new_depth_array.append(max_depth - 1)
                            known = True
                        else:
                            new_array.append(result[k])
                            new_depth_array.append(result_depth[k])
                    else:
                        known = False
                max_depth -= 1
                result = new_array
                result_depth = new_depth_array
            all_results.append(result)

            numbers_old = numbers_new

print(all_results)
result = max(all_results)

print("result: ", result)  
