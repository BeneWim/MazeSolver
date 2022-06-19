class Maze:
    def __init__(self, walls):
        self.walls = walls

    def is_wall(self, height, width):
        if height < 0 or height > len(self.walls[0]) -1:
            return True

        if width < 0 or width > len(self.walls) -1:
            return True

        if self.walls[width][height] == 1:
            return True

        return False

def crate_simple_maze(height, width):
    walls = [[0 for x in range(height)] for y in range(width)]

    walls[3][1] = 1
    walls[3][2] = 1
    walls[3][3] = 1
    walls[3][0] = 1

    walls[5][4] = 1
    walls[5][1] = 1
    walls[5][2] = 1
    #walls[5][3] = 1
    walls[8][4] = 1
    walls[8][2] = 1
    walls[8][3] = 1
    return Maze(walls)