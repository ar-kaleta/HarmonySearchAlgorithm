import time
from src.tsp import Tsp, generate_tsp_xls
from src.visualization import OutputData
from src.harmonySearchAlgorithm import algorithm
import matplotlib.pyplot as plt
start = time.time()


generate_tsp_xls(number_of_places=100, max_coordinate=50)
optimization_problem = Tsp()
output_data = OutputData([], [])
parameters = []
obj_functions = []
best_obj_fun = 1000000
# parameter = 10
# while parameter < 50:
x = algorithm(
    num_of_rows_hm=20,
    num_of_iterations=300000,
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
optimization_problem.visualize_solution(x[0])
# print(x[0].val_of_object_fun)

#print([x_.val_of_object_fun for x_ in x])
# print(x)

# plt.plot(parameters, obj_functions)
# plt.gca().invert_xaxis()
# plt.show()
print("execution time: " + str(time.time() - start))
