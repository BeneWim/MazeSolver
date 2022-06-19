import random

from Nodes.Node import Node

class Movement(Node):
    def __init__(self, entity):
        super().__init__(1, 0)
        self.entity = entity

        self.direction = random.randint(0, 3)

    def act(self, node, value):
        if value and not self.fired:
            self.fired = True

            if self.direction == 0:
                self.entity.move_right()

            if self.direction == 1:
                self.entity.move_down()

            if self.direction == 2:
                self.entity.move_left()

            if self.direction == 3:
                self.entity.move_up()