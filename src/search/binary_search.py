from typing import Any, List, Optional
from ..decorators import time_it


@time_it
def binary_search(value_to_search: Any, any_list: List[Any]) -> Optional[int]:
    """
    Search index position of value

    [args]
    - any_list : sorted array

    [returns]
    Array index position
    """
    lower_bound_index = 0
    upper_bound_index = len(any_list) - 1

    while lower_bound_index <= upper_bound_index:
        pivot_index = (lower_bound_index + upper_bound_index) // 2
        pivot_value = any_list[pivot_index]

        if value_to_search == pivot_value:
            return pivot_index

        elif value_to_search < pivot_value:
            upper_bound_index = pivot_index - 1

        else:
            lower_bound_index = pivot_index + 1
    return


# @time_it
def binary_search_recursive(
    value_to_search: Any, any_list: List[Any], lower_bound_index: int, upper_bound_index: int
) -> Optional[int]:
    if lower_bound_index > upper_bound_index:
        return None

    pivot_index = (lower_bound_index + upper_bound_index) // 2

    try:
        pivot_value = any_list[pivot_index]
        print(pivot_value)
    except IndexError:
        return None

    if value_to_search == pivot_value:
        print(f"will return {pivot_index}")
        return pivot_index

    if value_to_search < pivot_value:
        upper_bound_index = pivot_index - 1

    else:
        lower_bound_index = pivot_index + 1

    return binary_search_recursive(value_to_search, any_list, lower_bound_index, upper_bound_index)


def search_all_occurances(value_to_search: Any, any_list: List[Any]) -> List[int]:
    index_found = binary_search(value_to_search, any_list)
    print(f"Found at {index_found}")

    if index_found is None:
        return []

    occurence_index_list = [index_found]

    index_to_iterate_left = index_found - 1
    while index_to_iterate_left >= 0:
        if any_list[index_to_iterate_left] == value_to_search:
            occurence_index_list.append(index_to_iterate_left)
        else:
            break
        index_to_iterate_left -= 1

    index_to_iterate_right = index_found + 1
    while index_to_iterate_right < len(any_list):
        if any_list[index_to_iterate_right] == value_to_search:
            occurence_index_list.append(index_to_iterate_right)
        else:
            break
        index_to_iterate_right += 1

    return sorted(occurence_index_list)
