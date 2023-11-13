class VoidSquare:
    def __init__(self):
        self.possible_islands = []
        self.isisland = False
        #bin: 11
        self.color = 3

class Node:
    def __init__(self, true_index, target_size):
        self.true_index = true_index
        self.target_size = target_size
        self.size = 1
        self.locations = [true_index]
        self.possible_locations = []
        self.finish = target_size==self.size
        self.isisland = True
        #bin: 11
        self.color = 1
