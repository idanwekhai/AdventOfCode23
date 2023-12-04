with open('input.txt') as f:
  lines = [line.strip('\n') for line in f]

grid = [list(line) for line in lines]
edge_row = len(grid)-1
edge_col = len(grid[0])-1

def get_adj(i,j):
    if i == 0 and j == 0:
        down = grid[i+1][j]
        right = grid[i][j+1]
        down_right_diagonal = grid[i+1][j+1]
        return [down, right, down_right_diagonal]
    elif i == edge_row and j == edge_col:
        up = grid[i-1][j]
        left = grid[i][j-1]
        up_left_diagonal = grid[i-1][j-1]
        return [up, left, up_left_diagonal]
    elif i == 0 and j == edge_col:
        down = grid[i+1][j]
        left = grid[i][j-1]
        down_left_diagonal = grid[i+1][j-1]
        return [down, left, down_left_diagonal]
    elif i == edge_row and j == 0:
        up = grid[i-1][j]
        right = grid[i][j+1]
        up_right_diagonal = grid[i-1][j+1]
        return [up, right, up_right_diagonal]
    elif i == 0 and j < edge_col:
        down = grid[i+1][j]
        left = grid[i][j-1]
        right = grid[i][j+1]
        down_left_diagonal = grid[i+1][j-1]
        down_right_diagonal = grid[i+1][j+1]
        return [down, left, right, down_left_diagonal, down_right_diagonal]
    elif j == 0 and i < edge_row:
        up = grid[i-1][j]
        down = grid[i+1][j]
        right = grid[i][j+1]
        up_right_diagonal = grid[i-1][j+1]
        down_right_diagonal = grid[i+1][j+1]
        return [up, down, right, up_right_diagonal, down_right_diagonal]
    elif i == edge_row and j < edge_col:
        up = grid[i-1][j]
        left = grid[i][j-1]
        right = grid[i][j+1]
        up_right_diagonal = grid[i-1][j+1]
        up_left_diagonal = grid[i-1][j-1]
        return [up, left, right, up_right_diagonal, up_left_diagonal]
    elif j == edge_col and i < edge_row:
        up = grid[i-1][j]
        down = grid[i+1][j]
        left = grid[i][j-1]
        up_left_diagonal = grid[i-1][j-1]
        down_left_diagonal = grid[i+1][j-1]
        return [up, down, left, up_left_diagonal, down_left_diagonal]
    else:
        up = grid[i-1][j]
        down = grid[i+1][j]
        left = grid[i][j-1]
        right = grid[i][j+1]
        up_right_diagonal = grid[i-1][j+1]
        up_left_diagonal = grid[i-1][j-1]
        down_right_diagonal = grid[i+1][j+1]
        down_left_diagonal = grid[i+1][j-1]
        return [up, down, left, right, up_right_diagonal,
                up_left_diagonal, down_right_diagonal, down_left_diagonal]

def check_for_sym(lst):
    is_symbol = []
    for i in lst:
        if (str.isdigit(i)) or (i == '.'):
            is_symbol.append(False)
        else:
            is_symbol.append(True)
    return set(is_symbol)

nums_adj = []
num_track = ''
flag = False
for i in range(len(grid)):
    if num_track != '':
        nums_adj.append((num_track, flag))
        num_track = ''
        flag = False
    for j in range(len(grid[0])):
        idx_adj = get_adj(i, j)
        idx_adj_sym = check_for_sym(idx_adj)
        if grid[i][j] == '.' and num_track != '':
            nums_adj.append((num_track,flag))
            num_track = ''
            flag = False
        if len(idx_adj_sym) > 1:
            flag = True
        if str.isdigit(grid[i][j]):
            num_track += grid[i][j]
        else:
            if num_track != '':
                nums_adj.append((num_track,flag))
            num_track = ''
            flag = False
nums_adj.append((num_track,flag))
print(sum(map(int, [k for k,v in nums_adj if v])))
