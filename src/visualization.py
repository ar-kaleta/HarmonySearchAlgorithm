from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
from typing import List


class OutputData:
    def __init__(self, iteration, obj_function,
                 path1: str = '../data/obj_fun_data.xlsx'):
        self.obj_functions: List[int] = obj_function
        self.iterations: List[int] = iteration
        self.path_of_data = path1

    def add_data(self, iteration, obj_function):
        self.obj_functions.append(obj_function)
        self.iterations.append(iteration)

    def data_to_xls(self):
        df1 = DataFrame({
            'obj_function': self.obj_functions,
            'iterations': self.iterations})

        df1.to_excel(self.path_of_data, index=False)

    def plot_data(self):
        plt.plot(self.iterations, self.obj_functions)
        plt.show()

    def plot_data_in_init(self):
        plt.figure()
        self.guess_plot, = plt.plot([], [], 'b-')
        plt.xlabel('iter')
        plt.ylabel('cost')
        plt.draw()

    def add_data_to_plot(self, iterations, sp):
        self.guess_plot.set_xdata(np.append(self.guess_plot.get_xdata(), 1500 - iterations))
        self.guess_plot.set_ydata(np.append(self.guess_plot.get_ydata(), sp))

        plt.axis([min(self.guess_plot.get_xdata()), max(self.guess_plot.get_xdata()), min(self.guess_plot.get_ydata()),
                  max(self.guess_plot.get_ydata()) + 5])

        plt.pause(0.0001)
