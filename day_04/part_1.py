import numpy as np
with open('input') as f:
  lines = f.readlines()

  result = 0
  callingnumbers = lines[0].split(",")
# line 1 is zero
# line 2,3,4,5,6, is a bingo board
# line 7 is zero 
# line 8,9,10,11,12 is a bingo board
# line 13, 19, 25 are zero 
# etc....

# define bingo boards
  board_number = -1 # we are not yet on any board
  boards = np.zeros([100,5,5]) # define 100 boards with size 5x5
  for line in lines:
    n_line = lines.index(line)
    if n_line == 0: # skip the first line with the bingo numbers
      pass
    else:
      n_line = ((n_line-1)%6)
      if n_line == 0:
        board_number +=1 
      elif n_line != 0:
        new = line.split()
        for j in range(0,5):
          boards[board_number][n_line-1][j]= new[j]

  bingo = False
  for i in callingnumbers:
    if not bingo:
      # search for numbers
      for k in range(0,board_number+1):
        for j_1 in range(0,5):
          for j_2 in range(0,5):
            if int(boards[k][j_1][j_2]) == int(i):
              boards[k][j_1][j_2] = -1
      # check boards for bingo
      for k in range(0,board_number+1):
        for j_1 in range(0,5):
          for j_2 in range(0,5):
            sum_1 = np.sum(boards[k][j_1][:])
            sum_2 = np.sum(boards[k][:][j_2])
            if sum_1 == -5 or sum_2 == -5:
              bingo = True
              board = boards[k][:][:].flatten()
              print("bingo!")
              # overwrite -1:
              board = [0 if x==-1 else x for x in board]
              sum = np.sum(board)
              result = sum * int(i)

  print(result)