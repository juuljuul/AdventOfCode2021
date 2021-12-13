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

dots = np.zeros([m+1,m+1])
for i in range(0,len(x)):
        dots[int(x[i]), int(y[i])] = 1

# fold along x=655
for i in range(655+1, m+1):
    for j in range(0,m+1):
        if dots[i, j] == 1:
            dots[655-(i-655),j] = 1
            dots[i,j] = 0

print(dots.sum())
