from typing import Dict, Any


def flatten_dict(dictionary: Dict[Any, Any], parent_key: str = "", sep: str = "."):
    flattened_dict = {}
    for key, value in dictionary.items():
        new_key = parent_key + sep + key if parent_key else key
        if isinstance(value, dict):
            flattened_dict.update(flatten_dict(value, new_key, sep=sep))
        elif value is not None:
            flattened_dict[new_key] = value
    return flattened_dict
