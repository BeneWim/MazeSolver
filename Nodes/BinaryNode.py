from abc import abstractmethod

from Nodes.Node import Node

class BinaryNode(Node):
    def __init__(self):
        super().__init__(2, 1)

        self.first = None
        self.second = None

    def act(self, node, value):
        if not self.fired:
            if len(self.inputs) != 2:
                return

            if node.__eq__(self.inputs[0]):
                self.first = value

            if node.__eq__(self.inputs[1]):
                self.second = value

            if self.is_ready():
                self.fired = True

                self.send_response()

    def is_ready(self):
        if self.first is not None and self.second is not None:
            return True
        else:
            return False

    def send_response(self):
        response = self.get_response()

        for node in self.outputs:
            node.act(self, response)

        self.first = None
        self.second = None

    @abstractmethod
    def get_response(self):
        if not self.fired:
            self.fired = True

            # fire new nodes