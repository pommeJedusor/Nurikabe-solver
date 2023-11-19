from basic_funcs import *
from funcs1 import *
#size = int(input())
size = 5
#origin_grid = get_origin_grid(size=size)
origin_grid = [0 for i in range(size*size)]
origin_grid[5] = 1
origin_grid[14] = 3
origin_grid[18] = 4
origin_grid[20] = 2

grid = get_local_grid(origin_grid)
show_grid(grid, size)

get_all_paths_islands(grid, size)
for i in range(len(grid)):
    el = grid[i]
    if el.isisland() and el.origin_index==i:
        print(i)
        for path in el.paths:
            print(path)