from random import random
import time
from src.tsp import Tsp
from src.harmonyMemory import Harmony, HarmonyMemory, OptimizationProblem

t = time.clock()


def algorithm(
        num_of_rows_hm: int,
        num_of_cols_hm: int,
        num_of_iterations,
        hm_considering_rate,
        hm_pitch_adjusting_rate,
        hm_bandwidth,
        opt_problem: OptimizationProblem
) -> HarmonyMemory:

    # initialize the harmony memory randomly and calculate object function
    harmony_memory = HarmonyMemory(num_of_rows_hm, num_of_cols_hm, opt_problem)
    iteration = 1

    # main algorithm loop
    while iteration < num_of_iterations:
        new_harmony = []

        # iterating by notes in new harmony
        for note_index in range(0, len(harmony_memory[1])):
            # deciding if the next note should be generated or taken from memory
            if hm_considering_rate > random():
                rand_index = round(random() * (len(harmony_memory)-1))
                new_note = harmony_memory[rand_index][note_index]
                # deciding if the pitch adjusting mechanism should be used
                if hm_pitch_adjusting_rate > random():
                    tmp = -1
                    # check if temp is in range
                    while not 0 < tmp < 1:
                        # TODO: fix the following line coz is wrong
                        tmp = str(float(new_note) + hm_bandwidth * (random() - 0.5) * 1)
                    new_note = tmp
            else:
                # TODO: fix the following line coz is wrong
                new_note = opt_problem.generate_dec_variable()

            new_harmony.append(new_note)

        harmony_memory.harmonies.sort(key=lambda harmony: harmony.val_of_object_fun, reverse=True)
        # calculating new harmony objective function value
        val_of_object_fun = opt_problem.calculate_obj_fun(new_harmony)

        # comparing new harmony with the worst from the memory by the objective function and exchanging solutions
        if harmony_memory[len(harmony_memory)-1].val_of_object_fun < val_of_object_fun:
            harmony_memory[len(harmony_memory)-1].notes = new_harmony
            harmony_memory[len(harmony_memory)-1].val_of_object_fun = val_of_object_fun
        iteration = iteration + 1
    return harmony_memory


print(algorithm(
    num_of_rows_hm=100,
    num_of_cols_hm=100,
    num_of_iterations=100000,
    hm_considering_rate=0.9,
    hm_pitch_adjusting_rate=0.4,
    hm_bandwidth=0.01,
    opt_problem=Tsp()))

print(time.clock() - t)