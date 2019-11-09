from random import random
from typing import List, Any


class Harmony:
    def __init__(self, num_of_cols: int) -> None:
        self.notes = []
        self.val_of_object_fun = 0

        for col in range(0, num_of_cols):
            self.notes.append(random())
        self.val_of_object_fun = Harmony.calculate_obj_fun(self.notes)

    def __getitem__(self, item):
        return self.notes[item]

    def __setitem__(self, key, value):
        self.notes[key] = value

    def __str__(self):
        return str([self.val_of_object_fun] + self.notes)

    def __len__(self):
        return len(self.notes)

    @staticmethod
    def calculate_obj_fun(vector: List):
        return sum(vector)

    @staticmethod
    def generate_note():
        return random()


class HarmonyMemory:
    def __init__(self, num_of_rows: int, num_of_cols: int):
        self.harmonies: List[Harmony] = []

        for row in range(0, num_of_rows):
            self.harmonies.append(Harmony(num_of_cols))

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



