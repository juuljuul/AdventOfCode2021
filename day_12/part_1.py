import numpy as np
import re

with open('input') as f:   
    lines = f.readlines()

result = 0
rooms = ["start", "end"]

def find_path(matrix, line):
    global result
    new_matrix = matrix.copy()
    if small_rooms[line] == True:
        new_matrix[:,line] = 0
    for i in range(0, n_rooms):
    # find columns i with 1
        if matrix[line, i] == 1:
            #print("line, i, matrix[line,i]: ", line, i, matrix[line,i])
            # if small_rooms(i) is small, set column to 0
            if i == 1: # end reached, stop
                result += 1
                pass
            else:
            # go to line i, repeat
                find_path(new_matrix, i)

for line in lines:
    elements = re.split("-|\n", line)
    for x in elements:
        if x != "":
            if x not in rooms:
                rooms.append(x)
print("rooms: ", rooms)

# find small rooms
small_rooms = len(rooms)*[False]
for room in rooms:
    if room.islower():
        small_rooms[rooms.index(room)] = True
print(small_rooms)

# create adjacency matrix
n_rooms = int(len(rooms))
matrix = np.zeros([n_rooms,n_rooms])

for line in lines:
    for room1 in rooms:
        for room2 in rooms:
            if (room1 in line) and (room2 in line):
                if room1 != room2: #exclude staying in the same room
                    print("line, room1, room 2", line, room1, room2)
                    matrix[rooms.index(room1),rooms.index(room2)] = 1
                    matrix[rooms.index(room2),rooms.index(room1)] = 1
print(matrix)

find_path(matrix, 0)

'''
#1) start in first line to start at the start
for i in range(0, n_rooms):
    #2) find columns i with 1
    if matrix[1, i] == 1:
        #3) if small_rooms(i) is small, set column to 0
        if small_rooms[i] == True:
            matrix[:,i] = 0
        if i == 1: # end reached, stop
            continue
        else:
        #4) go to line i, repeat from 2
            pass
'''

print(result)