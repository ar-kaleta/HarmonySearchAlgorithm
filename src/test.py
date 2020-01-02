import time
start = time.time()
from src.tsp import Tsp, generate_tsp_xls, convert_txt_to_xls
from src.kp import Kp, generate_kp_xls
from src.outputData import OutputData
from src.harmonySearchAlgorithm import harmony_search_algorithm
start = time.time()

generate_tsp_xls(number_of_places=20, max_coordinate=5000)
optimization_problem = Tsp()
# optimization_problem.use_intercity_txt_data('gr17_d')

output_data = OutputData()
parameters = []
obj_functions = []
best_obj_fun = 1000000
num_of_rows_hm = 10
hm_pitch_adjusting_rate = 0.4
hm_bandwidth = 0.01

x = harmony_search_algorithm(
    num_of_rows_hm=num_of_rows_hm,
    num_of_iterations=100000,
    hm_considering_rate=0.9,
    hm_pitch_adjusting_rate=hm_pitch_adjusting_rate,
    hm_bandwidth=hm_bandwidth,
    opt_problem=optimization_problem,
    out_data=output_data)

output_data.plot_data('N = ' + str(num_of_rows_hm) + 'PAR = ' + str(hm_pitch_adjusting_rate) + 'BW = ' + str(hm_bandwidth))
output_data.data_to_xls()
print('N = ' + str(num_of_rows_hm) + 'PAR = ' + str(hm_pitch_adjusting_rate), 'BW = ' + str(hm_bandwidth))
print(x)

try:
    optimization_problem.visualise_solution(x[0])
except Exception as e:
    print(e)

print("execution time: " + str(time.time() - start))
