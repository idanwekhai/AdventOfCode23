import numpy as np
with open('input.txt') as f:
    grid = [list(line.strip('\n').split(' ')[0]) for line in f]

# map = {'|': 'NS','-': 'EW','L': 'NE', 'J': 'NW','7': 'SW', 'F': 'SE'}

#'.': 'Ground', 'S': 'Start'
grid = np.array(grid)
# print(grid)

map = {'L': '⎿', '7':'⏋',
      'F': '⎾', 'J':'⏌', '.':'.', 'G':'G'}


def walk_grid(i, j):
    pos = grid[i][j]
    up = grid[i-1][j]
    down = grid[i+1][j]
    left = grid[i][j-1]
    right = grid[i][j+1]


# if grid[i][j] == 'S' and 

start = ''
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'S':
            start = grid[i][j]
        if grid[i][j] in map:
            grid[i][j] = map[grid[i][j]]
print(grid)