import Nodes
from Entity import Entity
from Nodes.Movement import Movement
from Nodes.Not import Not
from Optimiser import Optimiser
from Visualizer import Visualizer
from Maze import crate_simple_maze


def init():
    height = 5
    width = 15

    maze = crate_simple_maze(height, width)

    visualizer = Visualizer(height, width, 40, maze)

    entity = Entity(maze)

    """"
    n = Not()
    entity.nodes.append(n)
    entity.starting_nodes[2].add_output(n)
    n.add_input(entity.starting_nodes[2])
    moving = Movement(entity)
    entity.nodes.append(moving)
    moving.add_input(n)
    n.add_output(moving)
    entity.print_information()
    print(entity.evaluate())
    """

    optimiser = Optimiser(entity, visualizer)
    #optimiser.visualizer.visualize_entity(entity)
    optimiser.start()

if __name__ == '__main__':
    init()

