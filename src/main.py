
import time
'''
from src.tsp import Tsp, generate_tsp_xls, convert_txt_to_xls
from src.kp import Kp, generate_kp_xls
from src.outputData import OutputData
from src.harmonySearchAlgorithm import harmony_search_algorithm
import matplotlib.pyplot as plt
start = time.time()

# generate_kp_xls()
# generate_tsp_xls(number_of_places=30, max_coordinate=5000)
convert_txt_to_xls('att48_xy', 'DataTsp')
optimization_problem = Tsp()
output_data = OutputData([], [])
parameters = []
obj_functions = []
best_obj_fun = 1000000
# parameter = 10
# while parameter < 50:
x = harmony_search_algorithm(
    num_of_rows_hm=40,
    num_of_iterations=1000000,
    hm_considering_rate=0.9,
    hm_pitch_adjusting_rate=0.4,
    hm_bandwidth=0.1,
    opt_problem=optimization_problem,
    out_data=output_data)
# parameter = int(1.1 * parameter)
output_data.plot_data()
output_data.data_to_xls()
# if best_obj_fun > x[0].val_of_object_fun:
#     best_obj_fun = x[0].val_of_object_fun
#     output_data.data_to_xls()
#     optimization_problem.print_solution(x[0])
# parameters.append(parameter)
# obj_functions.append(x[0].val_of_object_fun)
if optimization_problem.visualization:
    optimization_problem.visualise_solution(x[0])
# print(x[0].val_of_object_fun)

#print([x_.val_of_object_fun for x_ in x])
# print(x)

# plt.plot(parameters, obj_functions)
# plt.gca().invert_xaxis()
# plt.show()
print("execution time: " + str(time.time() - start))
'''

from itertools import combinations

from pandas import read_excel


def kp_xls_brute_force(filename, capacity):

    def anycomb(items):
        ' return combinations of any length from the items '
        return (comb
                for r in range(1, len(items) + 1)
                for comb in combinations(items, r)
                )

    def totalvalue(comb):
        ' Totalise a particular combination of items'
        totwt = totval = 0
        for item, wt, val in comb:
            totwt += wt
            totval += val
        return (totval, -totwt) if totwt <= capacity else (0, 0)

    df = read_excel('C:/Users/Artur/PycharmProjects/Harmony Search Algorithm/testcases/' + filename + '.xlsx')
    # data are saved as (place_id, x_coordinate, y_coordinate)
    items = tuple(((str(df.loc[i][0]), df.loc[i][1], df.loc[i][2]) for i in range(df.index[-1] + 1)))

    start = time.time()
    bagged = max(anycomb(items), key=totalvalue)
    print("execution time: " + str(time.time() - start))

    print("Bagged the following items\n  " +
          '\n  '.join(sorted(item for item,_,_ in bagged)))
    val, wt = totalvalue(bagged)
    print("for a total value of %i and a total weight of %i" % (val, -wt))


filename = 'kp29'
capacity = 1000
kp_xls_brute_force(filename, capacity)
