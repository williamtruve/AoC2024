import numpy as np
from tqdm import tqdm

# Read and parse the input file into a matrix
with open("input.txt", "r") as fp:
    matrix = np.array([list(line.strip()) for line in fp.readlines()])

# Find the starting position and define the direction mappings
start_pos = np.argwhere(matrix == "^")[0]
direction = (-1, 0)
direction_map = {
    (-1, 0): (0, 1),   # Up -> Right
    (0, 1): (1, 0),    # Right -> Down
    (1, 0): (0, -1),   # Down -> Left
    (0, -1): (-1, 0)   # Left -> Up
}

# Mark the starting position as visited
x, y = start_pos
matrix[x, y] = "X"

def walk(matrix, pos, direction):
    """
    Perform one step of the walk, turning if an obstacle is encountered.
    """
    x, y = pos
    try:
        while True:
            new_x, new_y = x + direction[0], y + direction[1]
            if matrix[new_x, new_y] != "#":
                break
            # Change direction if blocked
            direction = direction_map[direction]

        # Mark the new position as visited
        matrix[new_x, new_y] = "X"
        return matrix, (new_x, new_y), direction
    except IndexError:
        # If the new position is out of bounds, return without marking
        return matrix, (new_x, new_y), direction

LOOPS = 0

def solve(matrix, x, y, direction):
    """
    Simulate the guard's movement and detect loops.
    """
    global LOOPS
    visited = {(x, y, direction)}

    while 0 < x < matrix.shape[0] and 0 < y < matrix.shape[1]:
        matrix, (x, y), direction = walk(matrix, (x, y), direction)
        if (x, y, direction) in visited:
            LOOPS += 1  # Loop detected
            break
        visited.add((x, y, direction))
    return matrix

# Perform the initial simulation
matrix_copy = solve(matrix, x, y, direction)

# Find all positions visited during the simulation
possible_solutions = np.argwhere(matrix_copy == "X")

# Test each possible position for creating a loop
for test_pos in tqdm(possible_solutions):
    test_x, test_y = test_pos
    if (test_x, test_y) == (x, y):  # Skip the starting position
        continue

    # Temporarily place an obstacle and test for loops
    matrix[test_x, test_y] = "#"
    solve(matrix, x, y, direction)
    matrix[test_x, test_y] = "."  # Remove the obstacle after testing

# Output the total number of detected loops
print(LOOPS)