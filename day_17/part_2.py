import numpy as np

target_x = [179, 201]
target_y = [-109, -63]
#target_x = [20,30]
#target_y = [-10,-5]

start = [0,0]
result = 0

for velocity_x in range(0,target_x[1]*2):
    for velocity_y in range(-110, 300):
        x = start[0]
        y = start[0]
        y_max = 0
        v_x = velocity_x
        v_y = velocity_y
        while 1:
            # perform next step
            x = x + v_x
            y = y + v_y
            # physical forces on the velocities
            if v_x>0:
                v_x -= 1
            if v_x<0:
                v_x += 1
            v_y -= 1
            # check if in target area
            if x >= target_x[0] and x <= target_x[1] and y >= target_y[0] and y <= target_y[1]:
                result +=1
                break
            # check if out of bounds
            if x > 201 or x < -5 or y < -120:
                break 

print("result: ", result)