import numpy as np
import re

# init
diagram = np.zeros([1000,1000])
i = 0
x_s = []
y_s = []

with open('input') as f:
    lines = f.readlines()

    for line in lines:
        if "fold along" not in line and line != "\n":
            [x_,y_,z_]  = re.split(",|\n", line)
            x_s.append(x_)
            y_s.append(y_)

x = list(map(int, x_s))
y = list(map(int, y_s))

m = max(max(x), max(y))
print(m)

dots = np.zeros([m+1,m+1])
for i in range(0,len(x)):
        #print(x[i])
        dots[int(x[i]), int(y[i])] = 1

# foldinstructions
foldalong_axis = ["x", "y", "x", "y", "x", "y", "x", "y", "x", "y", "y", "y"]
foldalong_number = [655, 447, 327, 223, 163 , 111, 81, 55, 40, 27, 13, 6]

for fold_no in foldalong_number:

    # fold along x
    if foldalong_axis[foldalong_number.index(fold_no)] == "x":
        for j in range(0,m+1):
            dots[fold_no,j] = 0
            for i in range(fold_no+1, m+1):
                if dots[i, j] == 1:
                    dots[fold_no-(i-fold_no),j] = 1
                    dots[i,j] = 0

    # fold along y
    elif foldalong_axis[foldalong_number.index(fold_no)] == "y":
        for i in range(0, m+1):
            dots[i, fold_no] = 0
            for j in range(fold_no+1,m+1):
                if dots[i, j] == 1:
                    dots[i,fold_no-(j-fold_no)] = 1
                    dots[i, j] = 0
    else:
        print("something got wrong here:", foldalong_axis[foldalong_number.index(fold_no)])

new = open("part2", "w")
#new.write(dots)

for i in range(0,m+1):
    for j in range(0,m+1):
        if dots [j,i] == 1:
            new.write("#")
        else:
            new.write(".")
    new.write("\n")

