from itertools import combinations

from numpy import character

fp = open("input.txt", "r").readlines()

import numpy as np

matrix = []
characters = set()
for line in fp:
    row = []
    for c in line.strip():
        row.append(c)
        characters.add(c)
    matrix.append(row)
matrix = np.array(matrix)
characters.discard(".")
rows = matrix.shape[0]
cols = matrix.shape[1]

def find_antinode(pos1, pos2, lx, ly):
    x1, y1 = pos1
    x2, y2 = pos2

    dx, dy = (x1-x2, y1-y2)
    in_bounds = set()
    ix = 0
    while True:
        if 0 <= x1 + ix*dx < lx and 0 <= y1 + ix*dy < ly:
            in_bounds.add((x1 + ix*dx,y1 + ix*dy))
        else: break
        ix += 1

    ix = 0
    while True:
        if 0 <= x1 + ix*dx < lx and 0 <= y1 + ix*dy < ly:
            in_bounds.add((x1 + ix*dx,y1 + ix*dy))
        else: break
        ix -= 1
    return in_bounds


antinodes_matrix = np.copy(matrix)
antinodes_counter = 0
for key_char in characters:
    positions = np.argwhere(matrix == key_char)
    combs = (list(combinations(positions, 2)))
    for c in combs:
        nodes = (find_antinode(c[0], c[1], rows, cols))
        antinodes_counter += len(set(nodes))
        for node in nodes:
            antinodes_matrix[node] = "#"

print(len(np.argwhere(antinodes_matrix == "#")))
