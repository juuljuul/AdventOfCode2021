input = open("input", "r")

#initialize
result = 0
horizontal = 0
depth =  0

#calculate coordinates
for line in input:
    x = line.split()
    if x[0]=="up":
        depth-=int(x[1])
    if x[0]=="down":
        depth+=int(x[1])
    if x[0]=="forward":
        horizontal +=int(x[1])

print(horizontal*depth)

input.close()