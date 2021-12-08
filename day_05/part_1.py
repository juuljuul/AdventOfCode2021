import numpy as np
import re

# init
diagram = np.zeros([1000,1000])

with open('input') as f:
    lines = f.readlines()

    for line in lines:
        [x1,y1,x2,y2]  = re.split(" -> |,", line)
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)
        #print("x1 y1 x2 y2", x1, y1, x2, y2)
        if x1 == x2:
            if y2>y1:
                for y in range(y1,y2+1):
                    diagram[x1, y] +=1
            else:
                for y in range(y2,y1+1):
                    diagram[x1, y] +=1
        if y1 == y2:
            if x2>x1:
                for x in range(x1,x2+1):
                    diagram[x, y1] +=1
            else:
                for x in range(x2,x1+1):

                    diagram[x, y1] +=1

    diagram[diagram<2]=0

    result = np.count_nonzero(diagram)
    print("result: ", result)