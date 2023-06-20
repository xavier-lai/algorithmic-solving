from typing import List, Any


class HashTable:
    """HashTable = Dictionnary in python."""

    def __init__(self, max_length: int):
        self.max_length = max_length
        self.hash_list: List[Any] = [None for i in range(self.max_length)]

    def get_hash_index(self, any_key: str) -> int:
        hash_index = 0
        for character in any_key:
            hash_index += ord(character)  # str -> int with ascii
        return hash_index % self.max_length

    def set_value(self, any_key: str, value_to_set: Any):
        hash_index = self.get_hash_index(any_key)
        self.hash_list[hash_index] = value_to_set

    def get_value_from_key(self, any_key: str):
        key_index = self.get_hash_index(any_key)
        return self.hash_list[key_index]

    def delete_key(self, any_key: str):
        key_index = self.get_hash_index(any_key)
        self.hash_list[key_index] = None
