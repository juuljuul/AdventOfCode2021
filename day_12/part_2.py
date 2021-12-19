import numpy as np
import re
import time

tic = time.perf_counter()
with open('input') as f:  
    lines = f.readlines()

result = 0
rooms = ["start", "end"]

def find_path(matrix, line, visited_counter, double):
    global result
    new_matrix = matrix.copy()
    new_visited_counter = visited_counter.copy()
    if small_rooms[line] == True:
        new_visited_counter[line] += 1
        if any(x>1 for x in visited_counter):
            double = False
            new_matrix[:,line] = 0
        if double == False or line == 0:
            new_matrix[:,line] = 0
    for i in range(0, n_rooms):
    # find columns i with 1
        if matrix[line, i] == 1:
            if i == 1: # end reached, stop
                if any(x>2 for x in new_visited_counter) or len(new_visited_counter[new_visited_counter>=2])>1  :
                    pass
                else:
                    result += 1
                    pass
            else:
            # go to line i, repeat
                find_path(new_matrix, i, new_visited_counter, double)
 
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

visited_counter = np.zeros(len(rooms))
 
# create adjacency matrix
n_rooms = int(len(rooms))
matrix = np.zeros([n_rooms,n_rooms])
 
for line in lines:
    for room1 in rooms:
        for room2 in rooms:
            if (room1 in line) and (room2 in line):
                if room1 != room2: #exclude staying in the same room
                    matrix[rooms.index(room1),rooms.index(room2)] = 1
                    matrix[rooms.index(room2),rooms.index(room1)] = 1
print(matrix)
find_path(matrix, 0, visited_counter, True)
print(result)
toc = time.perf_counter()
print(f"caclulcation took {toc - tic:0.4f} seconds")
