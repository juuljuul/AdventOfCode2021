import numpy as np

input = open("input", "r")
result = 0
m = 100 # total number lines
n = 100 # total number columns

input_image = np.zeros([m,n])
n_line = 0
n_character = 0
algorithm = "####....#.....##.####..#.##.###.########.##.#..#.##.#...#..##.######..#......#..###.#.##.####.#.#.#....######.###...###.#.###.####..###.......#..#.#.#.#.#.####..####.#..####.#..####..##.#.#.#.###..##..#....#...###.#....###....##.###...##..#..#..#...##...#.#..#..###...####.#.#.###..#.#.#..###.##.##.#..###...#.#.#.##...#...#..#...##..###..###..#...###.#....#.##.#.####...##...##.#.####.#####.##...#######.###..##.#####.##.....####.#######.#.#.##....#...##...#..##.###.######.#######.#.#.#....#..##.###.#..##..##."

def transform(a):
    if a == ".":
        return(0)
    elif a == "#":
        return(1)
    else:
        raise ValueError("forbidden input for transform function")


# read in matrix
for line in input:
    for character in line:
        if character != "\n":
            input_image[n_line, n_character] = transform(character)
            n_character +=1
    n_line+=1
    n_character = 0

# count lit pixels in the beginning (4984)
print("lit pixels in the beginning: ", np.sum(input_image))

def calculate_new_image(image, n_lines, n_columns, surrounding):
    # since the image is "infinite", extend each side by 3
    if surrounding == 0:
        new_image = np.zeros([n_lines+6,n_columns+6])
    else:
        new_image = np.ones([n_lines+6,n_columns+6]) 
    for i in range(3,n_lines+3):
        for j in range(3,n_columns+3):
            new_image[i,j] = image[i-3, j-3]

    image = new_image
    # go through image to create the new image 
    if surrounding == 0:
        new_image = np.zeros([n_lines+6,n_columns+6])
    else:
        new_image = np.ones([n_lines+6,n_columns+6]) 
    for i in range(1,n_lines+5):
        for j in range(1,n_columns+5):
            square = image[i-1:i+2, j-1:j+2]
            square = square.astype(int)
            square = "".join(map(str,square.flatten()))
            new_image[i,j] = transform(algorithm[int(str(square), 2)])
            
    # cut the surrounding
    if surrounding == 0:
        new_new_image = np.zeros([n_lines+4,n_columns+4])
    else:
        new_new_image = np.ones([n_lines+4,n_columns+4]) 
    for i in range(0,n_lines+4):
        for j in range(0,n_columns+4):
            new_new_image[i,j] = new_image[i+1, j+1]

    #print(new_new_image)
    return(new_new_image)

first_image = calculate_new_image(input_image, m, n, 0)
print("lit pixels in the first image: ", np.sum(first_image))

second_image = calculate_new_image(first_image, m+4, n+4, 1)

result = np.sum(second_image)
print("result: ", result)

# 6280 is too high