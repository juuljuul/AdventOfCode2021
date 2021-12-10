import numpy as np

input = open("input", "r")

result = 0

for line in input:
    array = []
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
                if character == ")":
                    result += 3
                elif character == "]":
                    result += 57
                elif character == "}":
                    result += 1197
                elif character == ">":
                    result += 25137
                break
        elif character == "]":
            if array[-1] == "[":
                array.pop()
            else:
                if character == ")":
                    result += 3
                elif character == "]":
                    result += 57
                elif character == "}":
                    result += 1197
                elif character == ">":
                    result += 25137
                break
        elif character == "}":
            if array[-1] == "{":
                array.pop()
            else:
                if character == ")":
                    result += 3
                elif character == "]":
                    result += 57
                elif character == "}":
                    result += 1197
                elif character == ">":
                    result += 25137
                break
        elif character == ">":
            if array[-1] == "<":
                array.pop()
            else:
                if character == ")":
                    result += 3
                elif character == "]":
                    result += 57
                elif character == "}":
                    result += 1197
                elif character == ">":
                    result += 25137
                break
    else:
        pass
    
print("result:", result)

input.close()
