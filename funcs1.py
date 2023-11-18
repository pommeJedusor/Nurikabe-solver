from basic_funcs import *

def get_possible_moves(grid, size, index, possible_moves, origin_index):
    #up
    if index>=size and not index-size in possible_moves and grid[index-size].isavailable(grid, size, index-size, origin_index):
        possible_moves.append(index-size)
    #left
    if index%size and not index-1 in possible_moves and grid[index-1].isavailable(grid, size, index-1, origin_index):
        possible_moves.append(index-1)
    #right
    if (index+1)%size and not index+1 in possible_moves and grid[index+1].isavailable(grid, size, index+1, origin_index):
        possible_moves.append(index+1)
    #down
    if index<size*size-size and not index+size in possible_moves and grid[index+size].isavailable(grid, size, index+size, origin_index):
        possible_moves.append(index+size)


def get_all_paths(grid, size, index, origin_index, path, possible_moves, deep=0):
    path.append(index)
    if deep>=grid[origin_index].target_size-grid[origin_index].size:
        grid[origin_index].paths.append(copy_grid(path))
        path.remove(index)
        return grid[origin_index].paths
    get_possible_moves(grid, size, index, possible_moves, origin_index)
    for move in possible_moves:
        get_all_paths(grid, size, move, origin_index, path, possible_moves, deep+1)
    path.remove(index)
    return grid[origin_index].paths


def get_all_paths_islands(grid, size):
    for i in range(len(grid)):
        if grid[i].isisland() and grid[i].origin_index==i:
            grid[i].paths = get_all_paths(grid, size, i, i, [], [])