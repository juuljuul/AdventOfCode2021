import numpy as np

input = open("input", "r")

for line in input:
    lanternfish_s = line.split(",")

lanternfish = list(map(int, lanternfish_s)    )

# vector that contains on the i-th position the number of fish that are i days old
array_lanternfish = np.zeros(9)
days = 256

for i in lanternfish:
    array_lanternfish[i] +=1

for _ in range(0,days):
    for i in range(0,len(array_lanternfish)):
        if i == 0:
            baby = array_lanternfish[0]
        else:
            array_lanternfish[i-1] = array_lanternfish[i]
    array_lanternfish[6]=array_lanternfish[6]+baby
    array_lanternfish[8]=baby

print("result: ", sum(array_lanternfish))