input = open("input", "r")

#initialize
result = -1
previous_line = 0
previous_triple = 0
triple = 0
n_line = 0

#calculate result
for line in input:
    line = int(line)
    if n_line >=2:
        triple = pre_previous_line + previous_line + line
    if triple > previous_triple:
        result+=1
    n_line+=1
    pre_previous_line = previous_line
    previous_line = line
    previous_triple = triple

print(result)

input.close()
