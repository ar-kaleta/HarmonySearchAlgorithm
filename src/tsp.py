from random import randint, choice
from pandas import DataFrame, read_excel
from math import sqrt
from src.harmonyMemory import HarmonyMemory
from src.optimizationProblem import OptimizationProblem


def generate_tsp_xls(
        filename='Data',
        number_of_places=100,
        max_coordinate=50) -> None:
    x_coordinate = []
    y_coordinate = []
    coordinates = []
    places = []
    i = 1
    while len(places) < number_of_places:
        x = randint(0, max_coordinate)
        y = randint(0, max_coordinate)
        pair = (x, y)
        if pair not in coordinates:
            coordinates.append(pair)
            x_coordinate.append(x)
            y_coordinate.append(y)
            places.append(i)
            i += 1
    df = DataFrame({
        'place_id': places,
        'x_coordinate': x_coordinate,
        'y_coordinate': y_coordinate
    })
    df.to_excel('../testcases/' + filename + '.xlsx', index=False)


class Tsp(OptimizationProblem):
    def __init__(self, filename: str = 'Data'):
        df = read_excel('../testcases/' + filename + '.xlsx')
        self.data = {str(df.index[i]): (df.loc[i][1], df.loc[i][2]) for i in range(df.index[-1] + 1)}
        self.distance = count_distance(self.data)
        self.gain = 0

    def calculate_obj_fun(self, solution: list):
        distance = 0
        last_place = False
        for place in solution:
            if last_place:
                distance += self.distance[str(last_place)][str(place)]
            last_place = place
        return distance

    def generate_dec_variable(self, data: list) -> int:
        temp_data = list(set(self.data.keys()) - set(data))
        return choice(temp_data)

    # TODO: Test this function
    def take_dec_variable_hm(self, harmony_memory: HarmonyMemory, new_harmony: list, note_index: int) -> int:
        self.gain = 0

        while (note_index + self.gain) < len(harmony_memory[0])-1:
            # Try to find dec variable in note_index column of harmony memory
            [new_note, is_ok] = rand_note_for_note_index(harmony_memory, new_harmony, note_index+self.gain)
            if is_ok:
                return new_note
            else:
                # If it doesn't work try with next column
                self.gain += 1

        dec_variable_to_rand = list(set(harmony_memory[0])-set(new_harmony))
        new_note = choice(dec_variable_to_rand)
        return new_note

    # TODO: Fix and test this function
    def pitch_adj_mechanism(self, harmony_memory: HarmonyMemory, new_harmony: list, new_note: int, hm_bandwidth: float,
                            note_index: int) -> int:
        harmony_index = harmony_memory.index(new_note, note_index+self.gain)
        note_to_rand = []
        for note in harmony_memory[harmony_index]:
            if note not in new_harmony:
                note_to_rand.append(note)
        index = note_to_rand.index(new_note)
        index = int(index + hm_bandwidth * randint(-index, len(note_to_rand) - index))
        return note_to_rand[index]


def rand_note_for_note_index(harmony_memory: HarmonyMemory, new_harmony: list, note_index: int) -> [int, bool]:
    dec_variables: list = []
    note_index_ = note_index
    for elem in harmony_memory:
        dec_variables.append(elem[note_index_])
    dec_variable_to_rand = list(set(dec_variables) - set(new_harmony))
    if len(dec_variable_to_rand) is not 0:
        new_note = choice(dec_variable_to_rand)
        return [new_note, True]
    else:
        return [-1, False]


def count_distance(data: dict) -> dict:
    t_displacements = {}

    for start in data:
        temp_dict = {}
        for finish in data:
            if finish != start:
                x_displacement = data[finish][0] - data[start][0]
                y_displacement = data[finish][1] - data[start][1]
                displacement = sqrt(pow(x_displacement, 2) + pow(y_displacement, 2))
                temp_dict[finish] = displacement
        t_displacements[start] = temp_dict

    return t_displacements
