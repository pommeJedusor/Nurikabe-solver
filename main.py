"""
plan actuel
//done
pour chaque case obtenir les îles possibles:
    en faisant pour chaque île un algo DFS
    puis vérifier pour chaque case si ya un moyen de compléter l'île sans la case
        ajouter la case dans les must_pass_by
//not done
pour chaque case vide de 2x2:
    si une seule des case ne peut être accéder que par une île:
        ajouter la case dans les must_pass_by
    sinon si plusieurs des cases peuvent être accéder que par une seule île:
        ajouter la case 2x2 dans les must_pass_by
//not done

"""
from basic_funcs import *
from datas_struct import *
from funcs1 import *
from funcs2 import *

#size = int(input())
size = 5
#origin_grid = get_origin_grid(size=size)
origin_grid = [0 for i in range(size*size)]
origin_grid[5] = 1
origin_grid[14] = 3
origin_grid[18] = 4
origin_grid[20] = 2

show_grid(origin_grid, size=size)
grid = get_local_grid(origin_grid)

explore_islands(grid, size=size)
get_thing(grid, size)

#show grid
for i in range(size*size):
    square_index = i
    print(square_index)
    if grid[square_index].isisland:
        print(f"island: {grid[square_index].possible_locations}")
    else:
        print(grid[square_index].possible_islands)