from Nodes.Node import Node

class Not(Node):
    def __init__(self):
        super().__init__(1, 1)

    def act(self, node, value):
        if not self.fired:
            self.fired = True

            for node in self.outputs:
                node.act(node, not value)