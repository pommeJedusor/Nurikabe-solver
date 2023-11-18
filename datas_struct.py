class Square:
    def isisland(self):
        return self.color == 1
    def isavailable(self, grid, size, index, origin_index):
        #up
        if index>=size and grid[index-size].isisland() and grid[index-size].origin_index!=origin_index:
            return False
        #left
        if index%size and grid[index-1].isisland() and grid[index-1].origin_index!=origin_index:
            return False
        #right
        if (index+1)%size and grid[index+1].isisland() and grid[index+1].origin_index!=origin_index:
            return False
        #down
        if index<size*size-size and grid[index+size].isisland() and grid[index+size].origin_index!=origin_index:
            return False
        return True

class VoidSquare(Square):
    def __init__(self):
        #11 in bin
        self.color = 3
        self.possible_islands = []

class Island(Square):
    def __init__(self, index, size):
        #01 in bin
        self.origin_index = index
        self.color = 1
        self.target_size = size
        self.size = 1
        self.paths = []
        self.must_square = []
        self.extern_parts = []

    def is_extern(self, index):
        return index in self.extern_parts