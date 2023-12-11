import numpy as np
import itertools

with open('input.txt') as f:
    grid = [list(line.strip('\n').split(' ')[0]) for line in f]
grid = np.array(grid)

def get_distances(pairs, search):
    total = 0
    for i,j in pairs:
        Ax, Ay = search[i]
        Bx, By = search[j]
        distance = abs(Bx - Ax) + abs(By - Ay)
        total += distance
    return total

def space_idx(grid):
    idxs = []
    for i in range(len(grid)):
        if set(grid[i]) == {'.'}:
            idxs.append(i)
    return idxs

def get_galaxies_idx(grid, cols_idx, rows_idx, num=1):
    search = list(zip(*np.where(grid == '#')))
    new_idxs = []
    for i, j in search:
        row = i
        col = j
        for idx in range(row):
            if idx in rows_idx:
                row+=num-1
        for idx in range(col):
            if idx in cols_idx:
                col+=num-1
        new_idxs.append((row, col))
    return new_idxs


def solve(grid, expand):
    space_row_idx = space_idx(grid)
    space_col_idx = space_idx(grid.T)
    new_idxs = get_galaxies_idx(grid, space_col_idx, space_row_idx, expand)
    pairs_idx = list(itertools.combinations(range(len(new_idxs)), 2))
    total_path_lengths = get_distances(pairs_idx, new_idxs)
    return  total_path_lengths


print(solve(grid, expand=2))
print(solve(grid, expand=1_000_000))
