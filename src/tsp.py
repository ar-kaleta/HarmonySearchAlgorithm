from random import randint, choice
from pandas import DataFrame, read_excel
from math import sqrt
from src.harmonyMemory import OptimizationProblem


def generate_tsp_xls(
        filename='Data',
        number_of_places=100,
        max_coordinate=50) -> None:

    x_coordinate = []
    y_coordinate = []
    coordinates = []
    places = []

    for place_id in range(1, number_of_places+1):
        x = randint(0, max_coordinate)
        y = randint(0, max_coordinate)
        pair = (x, y)
        if pair not in coordinates:
            coordinates.append(pair)
            x_coordinate.append(x)
            y_coordinate.append(y)
            places.append(place_id)
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

    def calculate_obj_fun(self, solution: list):
        distance = 0
        last_place = False
        for place in solution:
            if last_place:
                a = self.distance[str(last_place)][str(place)]
                distance += self.distance[str(last_place)][str(place)]
            last_place = place
        return distance

    def generate_dec_variable(self, data: list) -> int:
        temp_data = list(set(self.data.keys()) - set(data))
        return choice(temp_data)


def count_distance(data: dict) -> dict:
    t_displacements = {}

    for start in data:
        temp_dict = {}
        for finish in data:
            if finish != start:
                a = data[finish][0]
                b = data[start][0]
                x_displacement = data[finish][0] - data[start][0]
                y_displacement = data[finish][1] - data[start][1]
                displacement = sqrt(pow(x_displacement, 2) + pow(y_displacement, 2))
                temp_dict[finish] = displacement
        t_displacements[start] = temp_dict

    return t_displacements
