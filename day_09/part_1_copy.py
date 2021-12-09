# copy for trying the example

import numpy as np

input = open("input_Ex", "r")
result = 0

floor = np.zeros([5,10]) # matrix for the floors
n_line = 0
n_character = 0

# read in matrix
for line in input:
    for character in line:
        if character != "\n":
            floor[n_line, n_character] = int(character)
            n_character +=1
    n_line+=1
    n_character = 0

#print(floor)
for i in range (1,4):
    for j in range (1,9):
        if floor[i,j]<floor[i-1,j] and floor[i,j]<floor[i+1,j] and floor[i,j]<floor[i,j-1] and floor[i,j]<floor[i,j+1]:
            result += (1+floor[i,j])
            print("here:::: ", floor[i,j])
# add border left
for i in range (1,4):
    if floor[i,0]<floor[i-1,0] and floor[i,0]<floor[i+1,0] and floor[i,0]<floor[i,1]:
        result += (1+floor[i,0])
        print("here: ", floor[i,0])
# add border right
for i in range (1,4):
    if floor[i,9]<floor[i-1,9] and floor[i,9]<floor[i+1,9] and floor[i,9]<floor[i,9-1]:
        result += (1+floor[i,9])
        print("here: ", floor[i,9])
# add border bottom
for j in range (1,9):
    print("bottom:", floor[4,j])
    print (floor[4-1,j], floor[4,j-1], floor[4,j+1])
    if (floor[4,j]<floor[4-1,j]) and (floor[4,j]<floor[4,j-1]) and (floor[4,j]<floor[4,j+1]):
        result += (1+floor[4,j])
        print("here: ", floor[4,j])
# add boder top
for j in range (1,9):
    print(floor[0,j])
    if floor[0,j]<floor[0+1,j] and floor[0,j]<floor[0,j-1] and floor[0,j]<floor[0,j+1]:
        result += (1+floor[0,j])
        print("here: ", floor[0,j])
# add corners
    # looked by eye: corners are no low points

print("result:", result)