import numpy as np

input = open("input", "r")

result = 0
octopi = -100*np.ones([12,12])
n_line = 1

# read in matrix
for line in input:
    n_character = 1
    for character in line:
        if character != "\n":
            octopi[n_line, n_character] = int(character)
            n_character +=1
    n_line+=1

# calculate new matrix
for _ in range (0,100):
    for i in range(1,11):
            for j in range(1,11):
                octopi[i,j] += 1
    new_octopi = octopi
    while np.any(new_octopi > 9):
        newnew_octopi = new_octopi
        for i in range(1,11):
            for j in range(1,11):
                if new_octopi[i,j] > 9:
                    result +=1
                    newnew_octopi[i,j] = 0
                    if newnew_octopi[i,j+1] > 0:
                        newnew_octopi[i,j+1] += 1
                    if newnew_octopi[i,j-1] > 0:
                        newnew_octopi[i,j-1] += 1
                    if newnew_octopi[i-1,j+1] > 0:
                        newnew_octopi[i-1,j+1] += 1
                    if newnew_octopi[i-1,j] > 0:
                        newnew_octopi[i-1,j] += 1
                    if newnew_octopi[i-1,j-1] > 0:
                        newnew_octopi[i-1,j-1] += 1
                    if newnew_octopi[i+1,j+1] > 0:
                        newnew_octopi[i+1,j+1] += 1
                    if newnew_octopi[i+1,j] > 0:
                        newnew_octopi[i+1,j] += 1
                    if newnew_octopi[i+1,j-1] > 0:
                        newnew_octopi[i+1,j-1] += 1
        newoctopi = newnew_octopi
    octopi = new_octopi

print("result:", result)

input.close()
