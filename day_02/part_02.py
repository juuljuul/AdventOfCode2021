input = open("input", "r")

#initialize
result = 0
horizontal = 0
depth =  0
aim = 0

#calculate coordinates
for line in input:
    x = line.split()
    if x[0]=="up":
        aim-=int(x[1])
    if x[0]=="down":
        aim+=int(x[1])
    if x[0]=="forward":
        horizontal +=int(x[1])
        depth+=(int(x[1])*aim)

print(horizontal * depth)

input.close()