from typing import List, Any


def quick_sort(any_list: List[Any]) -> List[Any]:
    length = len(any_list)

    if length <= 1:
        return any_list

    current_pivot = any_list[length // 2]
    lower_value_list = []
    equal_value_list = []
    upper_value_list = []

    for value_to_compare in any_list:
        if value_to_compare < current_pivot:
            lower_value_list.append(value_to_compare)
        elif value_to_compare == current_pivot:
            equal_value_list.append(value_to_compare)
        else:
            upper_value_list.append(value_to_compare)

    return quick_sort(lower_value_list) + equal_value_list + quick_sort(upper_value_list)
