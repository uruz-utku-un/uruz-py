# SPDX-License-Identifier: Uruz Open Commercial License (UOCL)-1.0
# Created: 2026-10-06
# Author: Uruz - Utku Ün (Kurt)
__version__ = "1.0.0"


import time


class UruzBenchmarkTester:
    """

    Methods:
        - `self`, `__str__()`:
    """


    def __init__(self):
        self.output_list = []  # çıktı listesi


    def __str__(self):
        """
        """
        separator = f"\n{79 * "-"}"
        executiontime_list = self._create_summary()
        return (
            f"\nExecution Time\n"
            f"{executiontime_list}"
            f"{separator}"
        )


    ### HELPER METHODS FOR REPORTING
    def _create_summary(self) -> str:
        """
        """
        return "\n".join(
            f"{status} {executiontime} {func_name}"
            for status, func_name, executiontime in self.output_list
        )


    def _append_result_executiontime(self, func_name: str, executiontime: float) -> None:
        """
        """
        result = ("[TIME]", func_name, executiontime)
        self.output_list.append(result)


    ### EXECUTION TIME TESTS ###
    def execution_time(self, func, *args, **kwargs) -> None:
        """
        """
        def measure_time(func, *args, **kwargs) -> float:
            """
            """
            start = time.perf_counter()
            func(*args, **kwargs)
            end = time.perf_counter()
            return end - start


        execution_time = measure_time(func, *args, **kwargs)
        self._append_result_executiontime(func_name=func.__name__, executiontime=execution_time)
        

        


# Practical test examples for the module.
# This code block does not run unless the module is executed directly.
if __name__ == "__main__":


    def print_numbers(numbers: list[int]) -> None:
        print(numbers)


    def sum_numbers_and_print(numbers: list[int]) -> None:
        print(sum(numbers))


    def sum_numbers_1loops_and_print(numbers: list[int]) -> None:
        sum_list = []
        for number_x in numbers:
            sum_list.append(number_x)

        print(sum(sum_list))


    def sum_numbers_2loops_and_print(numbers: list[int]) -> None:
        sum_list = []
        for number_x in numbers:
            sum_list.append(number_x)
            for number_y in numbers:
                sum_list.append(number_y)

        print(sum(sum_list))


    def sum_numbers_3loops_and_print(numbers: list[int]) -> None:
        sum_list = []
        for number_x in numbers:
            sum_list.append(number_x)
            for number_y in numbers:
                sum_list.append(number_y)
                for number_z in numbers:
                    sum_list.append(number_z)

        print(sum(sum_list))


    benchmark_tester = UruzBenchmarkTester()
    number_list = [0, 1, 2 , 3, 4, 5, 6, 7, 8, 9]
    benchmark_tester.execution_time(print_numbers, number_list)
    benchmark_tester.execution_time(sum_numbers_and_print, number_list)
    benchmark_tester.execution_time(sum_numbers_1loops_and_print, number_list)
    benchmark_tester.execution_time(sum_numbers_2loops_and_print, number_list)
    benchmark_tester.execution_time(sum_numbers_3loops_and_print, number_list)
    
    print(benchmark_tester)
