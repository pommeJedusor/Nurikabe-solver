"""
pour chaque case vide de 2x2:
    si une seule des case ne peut être accéder que par une île:
        ajouter la case dans les must_pass_by
    sinon si plusieurs des cases peuvent être accéder que par une seule île:
        ajouter la case 2x2 dans les must_pass_by
"""
from datas_struct import *

def get_thing(grid, size):
    for y in range(size-1):
        for x in range(size-1):
            island = -1
            index = -1
            #bottom left
            element = grid[y*size+x]
            #if there is an island in the 2x2 square or if an other move as alreay be seen
            if element.isisland or (len(element.possible_islands)>=1 and index!=-1) or len(element.possible_islands)>1:
                continue
            #if only one find in the 2x2 square for the moment
            elif len(element.possible_islands):
                index = y*size+x
                island = element.possible_islands[0]
            #bottom right
            element = grid[y*size+x+1]
            if element.isisland or (len(element.possible_islands)>=1 and index!=-1) or len(element.possible_islands)>1:
                continue
            elif len(element.possible_islands):
                index = y*size+x+1
                island = element.possible_islands[0]
            #top left
            element = grid[(y+1)*size+x]
            if element.isisland or (len(element.possible_islands)>=1 and index!=-1) or len(element.possible_islands)>1:
                continue
            elif len(element.possible_islands):
                index = (y+1)*size+x
                island = element.possible_islands[0]
            #top right
            element = grid[(y+1)*size+x+1]
            if element.isisland or (len(element.possible_islands)>=1 and index!=-1) or len(element.possible_islands)>1:
                continue
            elif len(element.possible_islands):
                index = (y+1)*size+x+1
                island = element.possible_islands[0]
            """
            problem:
            we could find a point but not be sure of the way the island should go to it
            in a way that we would have two part of an island
            """
            print("island")
            print(island)
            print(index)