from datas_struct import *

def copy_grid(grid):return [i for i in grid]

def get_local_grid(old_grid):
    grid = []
    for i in range(len(old_grid)):
        if old_grid[i]==0:
            grid.append(VoidSquare())
        else:
            grid.append(Island(i, old_grid[i]))
    return grid

def show_grid(grid, size):
    print("-"*round((size-5)/2)+"start"+"-"*round((size-5)/2))
    for i in range(size):
        for j in range(size):
            square = grid[i*size+j]
            if square.color == 2:
                print(end=" ")
            elif square.isisland():
                print(square.target_size,end="")
            else:
                print(end="0")
        print()
    print("-"*round((size-3)/2)+"end"+"-"*round((size-3)/2))