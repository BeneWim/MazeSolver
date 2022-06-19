import copy

import Config


class Optimiser:
    def __init__(self, entity, visualizer):
        self.entity = entity
        self.visualizer = visualizer

        self.generation = list()

        self.best_evaluation = 0

    def start(self):
        # self.visualizer.main_screen.after(0, self.run())
        # self.visualizer.main_screen.mainloop()
        self.run()

    def run(self):
        for _ in range(Config.get_number_of_generations()):
            self.manage_generation()
            self.entity.print_information()

        self.visualizer.visualize_entity(self.entity)

    def manage_generation(self):
        self.create_new_generation()
        self.mutate_generation()
        self.evaluate_generation()

    def create_new_generation(self):
        self.generation = list()

        for _ in range(Config.get_number_of_children_per_generation()):
            new_entity = copy.deepcopy(self.entity)
            self.generation.append(new_entity)

    def mutate_generation(self):
        for entity in self.generation:
            for _ in range(Config.get_number_of_mutations_per_cycle()):
                entity.mutate()

            entity.remove_unnecessary_nodes()

    def evaluate_generation(self):
        current_best_entity = None
        current_best_evaluation = 0

        for entity in self.generation:
            evaluation = entity.evaluate()

            if evaluation > current_best_evaluation:
                current_best_entity = entity
                current_best_evaluation = evaluation

        if current_best_evaluation > self.best_evaluation:
            self.entity = current_best_entity
            self.best_evaluation = current_best_evaluation