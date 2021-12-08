
new_file = open("part2_i1", "w")
new = open("part2_2", "w")
import numpy as np

#initialize
result = 0
column = 0
vector_0 = np.zeros(12)
vector_1 = np.zeros(12)

#calculate coordinates
for j in range(0,11):
    if j == 0:
        input = open("input", "r")
    elif (j % 2) == 1:
        input = open("part2_i1", "r")
    else:
        input = open("part2_2", "r")
    for line in input:
        if line[j] == "0":
            vector_0[j] += 1
        elif line[j] == "1" :
            vector_1[j] += 1

    input.close()
    if j == 0:
        input = open("input", "r")
    elif (j % 2) == 1:
        input = open("part2_i1", "r")
    else:
        input = open("part2_2", "r")

    if (j % 2) == 0:
        new_file = open("part2_i1", "w") 
    else:
        new_file = open("part2_2", "w")
    for line in input:
        if (vector_0[j]>vector_1[j] and line[j] == "0") or (vector_0[j]<vector_1[j] and line[j] == "1"):
            new_file.write(line)
    input.close()
    new_file.close()

b = np.zeros(12)

for j in range(0,12):
    if vector_0[j]>vector_1[j]:
        b[j] = 0
    else:
        b[j] = 1

print (b)

input.close()