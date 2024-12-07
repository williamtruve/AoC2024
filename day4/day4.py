from more_itertools.more import distinct_permutations

fp = open("input.txt", "r").readlines()
import numpy as np
matrix = []
for line in fp:
    row = []
    for c in line.strip():
        row.append(c)
    matrix.append(row)
matrix = np.array(matrix)
def step(matrix, pos, direction):
    x,  y = pos
    lx, ly = matrix.shape
    dx, dy = direction
    if (0 <= x+dx <= (lx - 1)) and (0 <= y+dy <= (lx - 1)):
        x += dx
        y += dy
    return (x,y), matrix[x,y]

def part_1(matrix, pos):
    directions = list(distinct_permutations([1,-1,0,-1,1], 2))
    xmases = 0
    for direction in directions:
        seq = [matrix[pos]]
        new_pos = pos
        for ix in range(len("XMAS")-1):
            new_pos, character = step(matrix, new_pos, direction)
            seq.append(character)
        score = int("".join(seq) in ["XMAS", "SAMX"])
        xmases += score
    return xmases
def part_2(matrix, pos):
    upleft = (-1, -1)
    upright = (1, -1)
    downright = (1,1)
    downleft = (-1, 1)
    center = matrix[pos]
    xes = ["SAM", "MAS"]
    _, c_1 = step(matrix, pos, downright)
    _, c_2 = step(matrix, pos, upleft)

    _, c_3 = step(matrix, pos, downleft)
    _, c_4 = step(matrix, pos, upright)

    return int((c_1 + center + c_2) in xes and c_3 + center + c_4 in xes)

p1_counter = 0
p2_counter = 0
for rx in range(len(matrix)):
   for cx in range(len(matrix)):
        p1_counter += part_1(matrix, (rx, cx))
        p2_counter += part_2(matrix, (rx, cx))
print(p1_counter//2)
print(p2_counter)