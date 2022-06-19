from time import sleep
from tkinter import *

import Config


class Visualizer:
    def __init__(self, height, width, box_size, maze):
        self.height = height
        self.width = width
        self.box_size = box_size
        self.maze = maze

        self.height_pixels = height * box_size
        self.width_pixels = width *box_size

        self.main_screen = Tk()

        self.canvas = Canvas(self.main_screen, width = self.width_pixels, height = self.height_pixels)

    def print_grid(self, entity):
        self.canvas.delete('all')

        self.print_goal_marker()
        self.print_maze()
        self.print_entity(entity)

        self.canvas.pack()
        self.main_screen.update()

    def print_maze(self):
        for width in range(self.width):
            for height in range(self.height):
                if self.maze.is_wall(height, width):
                    self.canvas.create_rectangle(width * self.box_size, height * self.box_size,
                        (width + 1) * self.box_size, (height + 1) * self.box_size, fill="blue", outline='blue')

    def print_entity(self, entity):
        self.canvas.create_rectangle(entity.width * self.box_size, entity.height * self.box_size,
            (entity.width + 1) * self.box_size, (entity.height + 1) * self.box_size, fill="red", outline='red')

    def print_goal_marker(self):
        self.canvas.create_rectangle((self.width - 1) * self.box_size, (self.height - 1) * self.box_size,
            self.width * self.box_size, self.height * self.box_size, fill="green", outline="green")

    def visualize_entity(self, entity):

        entity.reset_position()

        for _ in range(Config.get_number_of_evaluation_cycles()):
            self.print_grid(entity)
            entity.fire_starting_nodes()
            sleep(1)

        self.main_screen.mainloop()

