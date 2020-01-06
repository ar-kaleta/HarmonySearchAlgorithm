from abc import ABC, abstractmethod


class OptimizationProblem(ABC):
    @abstractmethod
    def calculate_obj_fun(self, harmony):
        pass

    @abstractmethod
    def generate_dec_variable(self, new_harmony: list) -> str:
        pass

    @abstractmethod
    def take_dec_variable_hm(self, harmony_memory, new_harmony: list, note_index: int) -> str:
        pass

    @abstractmethod
    def pitch_adj_mechanism(self, harmony_memory, new_harmony: list, new_note: str, hm_bandwidth: float,
                            note_index: int) -> str:
        pass

    @abstractmethod
    def complete_harmony(self):
        pass

    @abstractmethod
    def is_harmony_complete(self):
        pass

    @abstractmethod
    def visualise_solution(self, harmony):
        pass

    @abstractmethod
    def exchange_solution(self, worst_hm_obj_fun, new_sol_obj_fun) -> bool:
        pass

class DoNotUseLastReturnedValue(BaseException):
    pass
