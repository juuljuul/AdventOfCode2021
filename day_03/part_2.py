import numpy as np
input = open("input", "r")
array = input.readlines()

#initialize
result = 0
column = 0
vector_0 = np.zeros(12)
vector_1 = np.zeros(12)
i=0

#calculate coordinates
for j in range(0,12):
    new_array = []
    for i in array:
        if i[j] == "0":
            vector_0[j] += 1
        elif i[j] == "1" :
            vector_1[j] += 1

    for i in range(0,len(array)):
        if  (vector_0[j]<=vector_1[j] and array[i][j] == "0") or (vector_0[j]>vector_1[j] and array[i][j] == "1"):
            new_array.append(array[i])
    array = new_array
    if len(array)<=1:
        break

b = np.zeros(12)

for j in range(0,12):
    if vector_0[j]>vector_1[j]:
        b[j] = 0
    else:
        b[j] = 1

print (b)

input.close()