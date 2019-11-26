from typing import List
from src.optimizationProblem import OptimizationProblem


class Harmony:
    def __init__(self, num_of_cols: int, opt_problem: OptimizationProblem) -> None:
        self.notes = []
        self.val_of_object_fun = 0

        for col in range(0, len(opt_problem.data)):
            self.notes.append(opt_problem.generate_dec_variable(self.notes))
        self.val_of_object_fun = opt_problem.calculate_obj_fun(self.notes)

    def __getitem__(self, item):
        return self.notes[item]

    def __setitem__(self, key, value):
        self.notes[key] = value

    def __str__(self):
        return str([self.val_of_object_fun] + self.notes)

    def __len__(self):
        return len(self.notes)


class HarmonyMemory:
    def __init__(self, num_of_rows: int, num_of_cols: int, opt_problem: OptimizationProblem) -> None:
        self.harmonies: List[Harmony] = []

        for row in range(0, num_of_rows):
            self.harmonies.append(Harmony(num_of_cols, opt_problem))

    def __getitem__(self, item):
        return self.harmonies[item]

    def __setitem__(self, key, value):
        self.harmonies[key] = value

    def __str__(self):
        x: str = ''
        for elem in self.harmonies:
            x = x + str(elem) + '\n'
        return x

    def __len__(self):
        return len(self.harmonies)
