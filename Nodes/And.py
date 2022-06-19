from Nodes.BinaryNode import BinaryNode

class And(BinaryNode):
    def __init__(self):
        super().__init__()

    def get_response(self):
        return self.first and self.second