"""
pour chaque case obtenir les îles possibles:
    en faisant pour chaque île un algo DFS
    puis vérifier pour chaque case si ya un moyen de compléter l'île sans la case
        ajouter la case dans les must_pass_by
"""
from datas_struct import *
def location_available(node, grid, index, size):
    """return false if one of the square around `index` is another island than `node`"""
    #check top
    if index>=size and grid[index-size].isisland and not grid[index-size].true_index==node.true_index:
        return False
    #check left
    if index%size and grid[index-1].isisland and not grid[index-1].true_index==node.true_index:
        return False
    #check right
    if (index+1)%size and grid[index+1].isisland and not grid[index+1].true_index==node.true_index:
        return False
    #check bottom
    if index<size**2-size and grid[index+size].isisland and not grid[index+size].true_index==node.true_index:
        return False
    return True

def get_possible_squares(node, grid, index, size, deep=0, first_exe=False):
    """get the square that can be part of the island put them in `node.possible_locations` and `VoidSquare.possible_islands`"""
    #check if the square that we look is a part of the island
    if grid[index].isisland and not first_exe:
        return False
    #check if we're too far
    if node.target_size<deep+node.size:
        return False
    #get all possibles square for the island if first exploration
    if location_available(node, grid, index, size=size):
        if not first_exe and not node.true_index in grid[index].possible_islands:
            grid[index].possible_islands.append(node.true_index)
        if not first_exe and not index in node.possible_locations:
            node.possible_locations.append(index)
        #check by recursive the squares around if not already explored
        #up
        if index>=size:
            get_possible_squares(node, grid, index-size, size, deep+1, first_exe=False)
        #left
        if index%size:
            get_possible_squares(node, grid, index-1, size, deep+1, first_exe=False)
        #right
        if (index+1)%size:
            get_possible_squares(node, grid, index+1, size, deep+1, first_exe=False)
        #down
        if index< size**2-size:
            get_possible_squares(node, grid, index+size, size, deep+1, first_exe=False)

    return location_available(node, grid, index, size=size)

def extend_island(node, grid, index):
    """change the index to a part of the island of the `node`"""
    grid[index] = node
    node.size+=1
    node.locations.append(index)
    print(node.possible_locations)
    node.possible_locations.remove(index)
    node.finish = node.target_size==node.size
    if node.finish:
        print("finish")
        print(node.target_size)
        print(node.size)
        print(node.possible_locations)
        print(node.true_index)
        for loc in node.possible_locations:
            grid[loc].possible_islands.remove(node.true_index)
        node.possible_locations = []

def is_must_square(node, grid, index, square, temp_island, size):
    """
    return true if the square `index` must be in the island of the `node`
    """
    if index in temp_island:
        return 0
    if index==square:
        return 0
    if node==grid[index]:
        temp_island.append(index)
    elif type(grid[index])==Node:
        return 0
    elif node.true_index in grid[index].possible_islands:
        temp_island.append(index)
    else:
        return 0

    #up
    if index>=size:
        is_must_square(node, grid, index-size, square, temp_island, size=size)
    #left
    if index%size:
        is_must_square(node, grid, index-1, square, temp_island, size=size)
    #right
    if (index+1)%size:
        is_must_square(node, grid, index+1, square, temp_island, size=size)
    #down
    if index< size**2-size:
        is_must_square(node, grid, index+size, square, temp_island, size=size)
    
    if len(temp_island)>=node.target_size:
        return 0
    else:
        return 1

def get_must_squares(node, grid, index, size):
    """extent the island on the square that must be in the island of the node"""
    for square in [element for element in node.possible_locations]:
        result = is_must_square(node, grid, index, square, [], size=size)
        if result:
            extend_island(node, grid, square)
        
def explore_islands(grid, size):
    for i in range(size*size):
        if grid[i].isisland:
            get_possible_squares(grid[i],grid, i, size, first_exe=True)
    for i in range(size*size):
        if grid[i].isisland:
            get_must_squares(grid[i], grid, i, size=size)

def reset(grid, size):
    """reset exploration to avoid false datas"""
    for i in range(size*size):
        if not grid[i].isisland:
            grid[i].possible_islands = []
        else:
            grid[i].possible_locations = []