import numpy as np

input = open("input", "r")
result = 0

floor = np.zeros([100,100]) # matrix for the floors
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
for i in range (1,99):
    for j in range (1,99):
        if floor[i,j]<floor[i-1,j] and floor[i,j]<floor[i+1,j] and floor[i,j]<floor[i,j-1] and floor[i,j]<floor[i,j+1]:
            result += (1+floor[i,j])
# add border left
for i in range (1,99):
    if floor[i,0]<floor[i-1,0] and floor[i,0]<floor[i+1,0] and floor[i,0]<floor[i,1]:
        result += (1+floor[i,0])
# add border right
for i in range (1,99):
    if floor[i,99]<floor[i-1,99] and floor[i,99]<floor[i+1,99] and floor[i,99]<floor[i,99-1]:
        result += (1+floor[i,99])
# add border bottom
for j in range (1,99):
    print(floor[99,j])
    if floor[99,j]<floor[99-1,j] and floor[99,j]<floor[99,j-1] and floor[99,j]<floor[99,j+1]:
        result += (1+floor[99,j])
# add oder top
for j in range (1,99):
    print(floor[0,j])
    if floor[0,j]<floor[0+1,j] and floor[0,j]<floor[0,j-1] and floor[0,j]<floor[0,j+1]:
        result += (1+floor[0,j])
# add corners
    # looked by eye: corners are no low points

print(result)