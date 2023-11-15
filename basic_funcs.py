from datas_struct import *

def show_grid(grid, size):
    print("start")
    for y in range(size):
        for x in range(size):
            element = grid[y*size+x]
            if element.isisland:
                print(element.target_size,end="")
            elif element.possible_islands:
                print("0",end="")
            else:
                print(" ",end="")
        print("")
    print("-end-")

def get_origin_grid(size):
    origin_grid = []
    for i in range(size):
        for char in input():
            if char==".":
                origin_grid.append(0)
            elif char.isdigit():
                origin_grid.append(int(char))
    return origin_grid

def get_local_grid(origin_grid):
    grid = []
    for i in range(len(origin_grid)):
        element = origin_grid[i]
        if element:
            grid.append(Node(i, element))
        else:
            grid.append(VoidSquare())
    return grid