import random

import Config
from Nodes.And import And
from Nodes.Not import Not
from Nodes.Or import Or
from Nodes.Sensor import Sensor
from Nodes.Movement import Movement

class Entity:
    def __init__(self, maze):
        self.maze = maze

        self.nodes = list()
        self.starting_nodes = list()

        self.width = 1
        self.height = 1
        self.moves = 0

        self.add_sensors()

    def add_sensors(self):
        sensor_up = Sensor(self, "up")
        self.nodes.append(sensor_up)
        self.starting_nodes.append(sensor_up)

        sensor_down = Sensor(self, "down")
        self.nodes.append(sensor_down)
        self.starting_nodes.append(sensor_down)

        sensor_right = Sensor(self, "right")
        self.nodes.append(sensor_right)
        self.starting_nodes.append(sensor_right)

        sensor_left = Sensor(self, "left")
        self.nodes.append(sensor_left)
        self.starting_nodes.append(sensor_left)

    def fire_starting_nodes(self):
        for node in self.starting_nodes:
            node.act(None, None)

        self.reset_fired()

    def print_information(self):
        print("------------------")
        print("width: " + str(self.width) + " height: " + str(self.height) + " evaluation: " + str(self.evaluate()))
        for i in range(len(self.nodes)):
            print("Node " + str(i) + ": " + self.nodes[i].print_values())

    def mutate(self):
        chance = random.random()

        if chance < Config.get_new_node_probability():
            self.add_node()

        chance = random.random()

        if chance < Config.get_new_node_probability():
            self.add_connection()

    def add_node(self):
        node_number = random.randint(0, Config.get_number_of_nodes() - 1)

        if node_number == 0:
            self.nodes.append(And())

        if node_number == 1:
            self.nodes.append(Or())

        if node_number == 2:
            self.nodes.append(Not())

        if node_number == 3:
            self.nodes.append(Movement(self))

    def add_connection(self):
        node_from_index = random.randint(0, len(self.nodes) - 1)
        node_to_index = random.randint(0, len(self.nodes) - 1)

        node_from = self.nodes[node_from_index]
        node_to = self.nodes[node_to_index]

        if node_from.has_output_space() and node_to.has_input_space() and node_to_index != node_from_index:
            node_from.add_output(node_to)
            node_to.add_input(node_from)

    def __move(self, up, right):
        if not self.is_wall(up, right):
            self.width += right
            self.height += up
            self.moves += 1

    def move_up(self):
        self.__move(-1, 0)

    def move_right(self):
        self.__move(0, 1)

    def move_down(self):
        self.__move(1, 0)

    def move_left(self):
        self.__move(0, -1)

    def is_wall(self, up, right):
        return self.maze.is_wall(self.height + up, self.width + right)

    def reset_fired(self):
        for node in self.nodes:
            node.reset_fired()

    def evaluate(self):
        self.reset_position()
        self.moves = 0

        for i in range(Config.get_number_of_evaluation_cycles()):
            self.fire_starting_nodes()

        moves_to_target =  self.width + self.height

        return moves_to_target

    def reset_position(self):
        self.width = 0
        self.height = 0

    def remove_unnecessary_nodes(self):
        for node in self.nodes:
            if node in self.starting_nodes:
                continue

            if node.is_not_functional():
                self.nodes.remove(node)
