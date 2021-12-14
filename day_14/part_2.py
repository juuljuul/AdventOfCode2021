import numpy as np
import re
import pandas as pd

# init
steps = 40
polymer = "PHOSBSKBBBFSPPPCCCHN"
#polymer = "NNCB"
pairs = []
elements = []
existing_pairs = []


#polymer_chars = polymer.split("")
for i in range(0, len(polymer)-1):
    existing_pairs.append(polymer[i]+polymer[i+1])
count_existing_pairs = np.ones(len(existing_pairs))

with open('input') as f:
    lines = f.readlines()

    for line in lines:
        [pair,element,_]  = re.split(" -> |\n", line)
        pairs.append(pair)
        elements.append(element)

for _ in range(0,steps):
    new_existing_pairs = []
    new_count_existing_pairs = []
    for i in range(0, len(existing_pairs)):
        exists = 0
        for j in range(0,len(pairs)):
            if existing_pairs[i] == pairs[j]:
                exists = 1
                a = "".join([existing_pairs[i][0], elements[j]])
                b = "".join([elements[j], existing_pairs[i][1]])
                if a in new_existing_pairs:
                    new_count_existing_pairs[new_existing_pairs.index(a)] += count_existing_pairs[i]
                else:
                    new_existing_pairs.append(a)
                    new_count_existing_pairs.append(count_existing_pairs[i])
                if b in new_existing_pairs:
                    new_count_existing_pairs[new_existing_pairs.index(b)] += count_existing_pairs[i]
                else:
                    new_existing_pairs.append(b)
                    new_count_existing_pairs.append(count_existing_pairs[i])
        if exists == 0:
            print("pair does not exist!")
            pass
    existing_pairs = new_existing_pairs
    count_existing_pairs = new_count_existing_pairs

# count letters
letters = []
n_letters = []
for element in existing_pairs:
    if element[0] in letters:
        n_letters[letters.index(element[0])] += count_existing_pairs[existing_pairs.index(element)]
    else:
        letters.append(element[0])
        n_letters.append(count_existing_pairs[existing_pairs.index(element)])

n_letters[letters.index(polymer[-1])] += 1

print("letters ", letters)
print("result: ", max(n_letters)-min(n_letters))
