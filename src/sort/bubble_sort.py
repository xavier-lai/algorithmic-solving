from typing import Any, List

from ..decorators import time_it


@time_it
def bubble_sort(any_list: List[Any]) -> List[Any]:
    length = len(any_list)

    at_least_on_swap_occured = False
    for iteration_count in range(length - 1):
        for index in range(length - 1 - iteration_count):
            if any_list[index] > any_list[index + 1]:
                tmp_current_value = any_list[index]
                any_list[index], any_list[index + 1] = any_list[index + 1], tmp_current_value
                at_least_on_swap_occured = True
        if at_least_on_swap_occured is False:
            return any_list
    return any_list
