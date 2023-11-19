from basic_funcs import *

def check_path(path, all_paths):
    for all_p in all_paths:
        for i in range(len(path)):
            if path[i]!=all_p[i]:
                break
        else:
            return True
    return False

def get_possible_moves(grid, size, index, possible_moves, origin_index):
    moves = []
    #up
    if index>=size and not index-size in possible_moves and grid[index-size].isavailable(grid, size, index-size, origin_index):
        possible_moves.append(index-size)
        moves.append(index-size)
    #left
    if index%size and not index-1 in possible_moves and grid[index-1].isavailable(grid, size, index-1, origin_index):
        possible_moves.append(index-1)
        moves.append(index-1)
    #right
    if (index+1)%size and not index+1 in possible_moves and grid[index+1].isavailable(grid, size, index+1, origin_index):
        possible_moves.append(index+1)
        moves.append(index+1)
    #down
    if index<size*size-size and not index+size in possible_moves and grid[index+size].isavailable(grid, size, index+size, origin_index):
        possible_moves.append(index+size)
        moves.append(index+size)
    return moves


def get_all_paths(grid, size, index, origin_index, path, possible_moves, deep=0):
    #insert index in path
    if index in path:
        return grid[origin_index].paths
    for i in range(len(path)):
        if path[i]>index:
            path.insert(i, index)
            break
    else:
        path.append(index)
    
    if check_path(path, grid[origin_index].paths):
        path.remove(index)
        return grid[origin_index].paths

    if deep>=grid[origin_index].target_size-grid[origin_index].size:
        grid[origin_index].paths.append(copy_grid(path))
        path.remove(index)
        return grid[origin_index].paths

    moves = get_possible_moves(grid, size, index, possible_moves, origin_index)
    all_moves = [move for move in possible_moves]
    all_moves.sort()
    for move in all_moves:
        possible_moves.remove(move)
        get_all_paths(grid, size, move, origin_index, path, possible_moves, deep+1)
        possible_moves.append(move)
    for move in moves:
        possible_moves.remove(move)
    path.remove(index)
    return grid[origin_index].paths


def get_all_paths_islands(grid, size):
    for i in range(len(grid)):
        if grid[i].isisland() and grid[i].origin_index==i:
            grid[i].paths = get_all_paths(grid, size, i, i, [], [])

def get_must_squares(grid, size):
    for i in range(size*size):
        if not grid[i].isisland():
            continue
        optionnal_squares = []
        must_squares = grid[i].paths[0]
        for path in grid[i].paths[1:]:
            squares = []
            for index in path:
                if index in optionnal_squares or not index in must_squares:
                    continue
                else:
                    squares.append(index)
            must_squares = squares

        grid[i].must_squares = must_squares