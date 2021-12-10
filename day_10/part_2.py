import numpy as np

input = open("input", "r")

result = 0
line_results = []

for line in input:
    array = []
    line_result = 0
    for character in line:
        if character == "(":
            array.append(character)
        elif character == "[":
            array.append(character)
        elif character == "{":
            array.append(character)
        elif character == "<":
            array.append(character)
        elif character == ")":
            if array[-1] == "(":
                array.pop()
            else:
                break
        elif character == "]":
            if array[-1] == "[":
                array.pop()
            else:
                break
        elif character == "}":
            if array[-1] == "{":
                array.pop()
            else:
                break
        elif character == ">":
            if array[-1] == "<":
                array.pop()
            else:
                break
        elif character == "\n":
            array.reverse()
            for element in array:
                if element == "(":
                    line_result = line_result *5 + 1
                elif element == "[":
                    line_result = line_result *5 + 2
                elif element == "{":
                    line_result = line_result *5 + 3
                elif element == "<":
                    line_result = line_result *5 + 4
            line_results.append(line_result)
    else:
        pass

line_results.sort()
middleIndex = int((len(line_results) - 1)/2)

print("result: ", line_results[middleIndex])

input.close()
