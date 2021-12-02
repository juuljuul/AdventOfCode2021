input = open("input", "r")

# initializtaion
result = -1
pre = 0

# calculate result
for line in input:
    line = int(line)
    if pre > line:
        result+=1
    pre = line

#print result
print(result)

input.close()
