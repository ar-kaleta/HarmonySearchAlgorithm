import time

from pandas import DataFrame

start = time.time()
from src.tsp import Tsp, generate_tsp_xls, convert_txt_to_xls
from src.kp import Kp, generate_kp_xls
from src.outputData import OutputData
from src.harmonySearchAlgorithm import harmony_search_algorithm
start = time.time()

optimization_problem = Kp('parameterKpTest')

output_data = OutputData()
parameters = []
obj_functions = []
best_obj_fun = 1000000
num_of_rows_hm = 10
hm_pitch_adjusting_rate = 0.45
hm_bandwidth = 0.1
for parameter in range(1, 10, 1):
    parameter = float(parameter)*0.1
    vals = []
    for i in range(5):
        x = harmony_search_algorithm(
            num_of_rows_hm=num_of_rows_hm,
            num_of_iterations=100000,
            hm_considering_rate=parameter,
            hm_pitch_adjusting_rate=hm_pitch_adjusting_rate,
            hm_bandwidth=hm_bandwidth,
            opt_problem=optimization_problem,
            out_data=output_data)
        vals.append(x[0].val_of_object_fun)
    parameters.append(parameter)
    obj_functions.append(sum(vals)/len(vals))

df1 = DataFrame({
    'parameter': parameters,
    'mean_of_obj_fun': obj_functions})

df1.to_excel('C:/Users/Artur/PycharmProjects/Harmony Search Algorithm/data/tests/KP/test_HMCR_parameter.xlsx', index=False)



print("execution time: " + str(time.time() - start))
