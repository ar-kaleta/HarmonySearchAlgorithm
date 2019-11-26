from abc import ABC, abstractmethod



class OptimizationProblem(ABC):
    @abstractmethod
    def calculate_obj_fun(self, solution):
        pass

    @abstractmethod
    def generate_dec_variable(self, data: list) -> int:
        pass

    @abstractmethod
    def take_dec_variable_hm(self, harmony_memory, new_harmony: list, note_index: int) -> [int, int]:
        pass

    @abstractmethod
    def pitch_adj_mechanism(self, harmony_memory, new_harmony: list, new_note: int, hm_bandwidth: float,
                            harmony_index: int) -> int:
        pass
