import numpy as np
import math

result = 0

with open('input') as f:
    line = f.readlines()

# convert into binary
binary_value = bin(int(line[0], base=16))[2:]
binary_value = binary_value.zfill(math.ceil(len(binary_value)/4)*4)
print(binary_value)
print("length: ", len(binary_value))

# write in a list
binary_vector = []
for character in binary_value:
    binary_vector.append(character)
print(binary_vector)

# i is the start value of a packet
i = 0

while i < (len(binary_vector)-3):
    # first three bits: packet version
    packet_version = int(''.join([binary_vector[i], binary_vector[i+1], binary_vector[i+2]]), 2)
    i +=3
    if i>len(binary_vector)-3:
        print("break at i = ", i)
        break
    print("packet_version: ", packet_version)
    result += packet_version
    #print("version no ", packet_version)
    # second three bits: type ID
    type_ID = int(''.join([binary_vector[i], binary_vector[i+1], binary_vector[i+2]]), 2)
    #print("type ID: ", type_ID)
    i +=3
    if i>len(binary_vector):
        break
    if type_ID == 4:
        in_packet = True
        while in_packet == True:
            i += 5
            if i>len(binary_vector):
                break
            if binary_vector[i-5] == '0': #last packet
                in_packet = False
                break
    else:
        #print("operator at i = , binary_vector[i], ", i, binary_vector[i])
        if binary_vector[i] == '0':
            i += 16
        else: #(i == 0):
            i += 12
    
    # type ID != 4: operator: performs calculation on subpackets within
        # length type ID: 7th value in packet
        # length type ID == 0:the next 15 bits are a number that represents the total length in bits of the sub-packets contained by thins packet
        # length type ID == 1: next 11 bits are number of sub-packets immediately cotained by this packet

    

# result is sum of all version numbers

print("result: ", result)