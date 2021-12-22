import numpy as np
import re

input = open("input", "r")

result = 0
cube = np.zeros(shape=(101,101,101))
regex = "(on|off)\sx=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)"

for line in input:
    step = re.match(regex, line)
    # command = step[1]
    # x = step[2:3]
    # y = step[4:5]
    # z = step[6:7]
    if abs(int(step[2]))>50 or abs(int(step[3]))>50 or abs(int(step[4]))>50 or abs(int(step[5]))>50 or abs(int(step[6]))>50 or abs(int(step[7]))>50:
        continue
    if step[1] == "on":
        print("switch on")
        command = 1
    if step[1] == "off":
        print("switch off")
        command = 0
    for x in range(int(step[2]), int(step[3])+1):
        for y in range(int(step[4]), int(step[5])+1):
            for z in range(int(step[6]), int(step[7])+1):
                if abs(x)<=50 and abs(y)<=50 and abs(z)<=50:
                    cube[x,y,z] = command

print("result:", np.sum(cube))

input.close()
