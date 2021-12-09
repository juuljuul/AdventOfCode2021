# copy for trying the example

import numpy as np
import re

input = open("input", "r")
result = 1

floor = 9*np.ones([102,102]) # matrix for the floors
visited = np.zeros([102,102])
basins = []
n_line = 1
n_character = 1
size = 0

def go(i,j):
    visited[i,j] = 1
    size = 1
    if floor[i-1,j] != 9:
        if visited[i-1,j] == 0:
            size += go(i-1,j)
    if floor[i+1,j] != 9:
        if visited[i+1,j] == 0:
            size += go(i+1,j)
    if floor[i,j-1] != 9:
        if visited[i,j-1] == 0:
            size += go (i,j-1)
    if floor[i,j+1] != 9:
        if visited[i,j+1] == 0:
            size += go (i,j+1)
    return(size)

# read in matrix
for line in input:
    for character in line:
        if character == "9":
            floor[n_line, n_character] = int(character)
            n_character +=1
        elif character != "\n":
            floor[n_line, n_character] = 0
            n_character +=1
    n_line+=1
    n_character = 1

for i in range (1,101):
    for j in range (1,101):
        if visited[i,j] == 0:
            size = 0
            basins.append(go(i,j))

# somehow each numer is one too high
basins[:] = [x - 1 for x in basins]

result *=max(basins)
basins.remove(max(basins))
result *=max(basins)
basins.remove(max(basins))
result *=max(basins)

print(result)