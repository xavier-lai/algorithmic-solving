from typing import Any, List, Optional


class HashTable:
    """HashTable = Dictionnary in python."""

    def __init__(self, max_length: int):
        self.max_length = max_length
        self.hash_list: List[List[Any]] = [[] for i in range(self.max_length)]

    def get_hash_index(self, any_key: str) -> int:
        hash_index = 0
        for character in any_key:
            hash_index += ord(character)  # str -> int with ascii
        return hash_index % self.max_length

    def set_value(self, any_key: str, value_to_set: Any):
        hash_index = self.get_hash_index(any_key)
        key_is_found = False
        for current_tuple_index, current_tuple in enumerate(self.hash_list[hash_index]):
            if len(current_tuple) == 2 and current_tuple[0] == any_key:
                key_is_found = True
                self.hash_list[hash_index][current_tuple_index] = (any_key, value_to_set)
                break

        if not key_is_found:
            self.hash_list[hash_index].append((any_key, value_to_set))

    def get_value_from_key(self, any_key: str) -> Optional[Any]:
        hash_index = self.get_hash_index(any_key)
        for current_tuple in self.hash_list[hash_index]:
            if current_tuple[0] == any_key:
                return current_tuple[1]

    def delete_key(self, any_key: str):
        hash_index = self.get_hash_index(any_key)
        for current_tuple_index, current_tuple in enumerate(self.hash_list[hash_index]):
            print(current_tuple)
            if current_tuple[0] == any_key:
                del self.hash_list[hash_index][current_tuple_index]
                break
