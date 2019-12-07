from typing import List
from src.optimizationProblem import OptimizationProblem


class Harmony:
    def __init__(self, opt_problem: OptimizationProblem) -> None:
        self.notes = []
        self.val_of_object_fun = 0
        is_complete = 0

        while not is_complete:
            [new_note, is_complete] = opt_problem.generate_dec_variable(self.notes)
            self.notes.append(new_note)
        self.val_of_object_fun = opt_problem.calculate_obj_fun(self.notes)

    def __getitem__(self, item):
        return self.notes[item]

    def __setitem__(self, key, value):
        self.notes[key] = value

    def __str__(self):
        return str([self.val_of_object_fun] + self.notes)

    def __len__(self):
        return len(self.notes)

    def __eq__(self, other: (list, float)):
        if self.val_of_object_fun != other[1]:
            return False
        for self_note, other_note in zip(self.notes, other[0]):
            if self_note != other_note:
                return False
        return True


class HarmonyMemory:
    def __init__(self, num_of_rows: int, opt_problem: OptimizationProblem) -> None:
        self.harmonies: List[Harmony] = []

        for row in range(0, num_of_rows):
            self.harmonies.append(Harmony(opt_problem))

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

    def index(self, value_to_find: int, note_index):
        for index in range(0, len(self.harmonies)):
            if self.harmonies[index][note_index] == value_to_find:
                return index
        return -1
