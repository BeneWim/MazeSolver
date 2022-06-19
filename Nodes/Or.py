from Nodes.BinaryNode import BinaryNode

class Or(BinaryNode):
    def __init__(self):
        super().__init__()

    def get_response(self):
        return self.first or self.second