import numpy as np

input = open("input", "r")

for line in input:
    crabs_s = line.split(",")

crabs = list(map(int, crabs_s)    )

m = max(crabs)

def count_steps(steps):
    res = 0
    for i in range(0,steps + 1):
        res += (i)
    return(res)

array = []
for i in range(0, m+1):
    new_array = [count_steps(abs(x-i)) for x in crabs]
    array.append(sum(new_array))

result = min(array)
print(result)

