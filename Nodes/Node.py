from abc import abstractmethod

class Node:
    def __init__(self, max_in, max_out):
        self.max_in = max_in
        self.max_out = max_out

        self.inputs = list()
        self.outputs = list()

        self.fired = False

    def print_values(self):
        return str(self) + ": " + str(self.max_in) + ": " + str(self.inputs) + ", " + str(self.max_out) + ": " + str(self.outputs)

    def add_input(self, node):
        if len(self.inputs) < self.max_in:
            self.inputs.append(node)

    def add_output(self, node):
        if len(self.outputs) < self.max_out:
            self.outputs.append(node)

    def has_input_space(self):
        if len(self.inputs) < self.max_in:
            return True
        else:
            return False

    def has_output_space(self):
        if len(self.outputs) < self.max_out:
            return True
        else:
            return False

    def reset_fired(self):
        self.fired = False

    def is_not_functional(self):
        return len(self.inputs) != self.max_in and len(self.outputs) == 0

    @abstractmethod
    def act(self, node, value):
        pass