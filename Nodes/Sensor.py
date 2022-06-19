from Nodes.Node import Node

class Sensor(Node):
    def __init__(self, entity, direction):
        super().__init__(0, 10000000)

        self.entity = entity

        self.up = 0
        self.right = 0

        if direction == 'up':
            self.up = -1
        elif direction == 'down':
            self.up = 1
        elif direction == 'left':
            self.right = -1
        elif direction == 'right':
            self.right = 1

    def act(self, node, value):
        if not self.fired:
            self.fired = True

            is_wall = self.entity.is_wall(self.up, self.right)

            for node in self.outputs:
                node.act(self, is_wall)