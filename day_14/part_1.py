import numpy as np
import re
import pandas as pd

# init
diagram = np.zeros([1000,1000])
steps = 10
polymer = "PHOSBSKBBBFSPPPCCCHN"
#polymer = "NNCB"
pairs = []
elements = []

with open('input') as f:
    lines = f.readlines()

    for line in lines:
        [pair,element,_]  = re.split(" -> |\n", line)
        pairs.append(pair)
        elements.append(element)

for _ in range(0,steps):
    polymer_new = []
    for i in range(0, len(polymer)):
        polymer_new.append(polymer[i])
        if i < len(polymer)-1:
            for j in range(0,len(pairs)):
                if polymer[i] == pairs[j][0] and polymer[i+1] == pairs[j][1]:
                    polymer_new.append(elements[j])
    polymer = polymer_new

# count letters
print(pd.Series(list(polymer)).value_counts())