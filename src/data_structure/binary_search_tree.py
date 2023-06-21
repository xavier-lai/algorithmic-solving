from typing import Any, List


class BinarySearchTree:
    def __init__(self, data: Any):
        self.data = data
        self.left = None
        self.right = None

    def add_child_node(self, data: Any):
        if self.data == data:
            return

        if data < self.data:
            if self.left is not None:
                self.left.add_child_node(data)
            else:
                self.left = BinarySearchTree(data)

        else:
            if self.right is not None:
                self.right.add_child_node(data)
            else:
                self.right = BinarySearchTree(data)

    def sort_ascending(self) -> List[Any]:
        sorted_list = []

        if self.data is None:
            return sorted_list

        if self.left is not None:
            sorted_list += self.left.sort_ascending()

        sorted_list.append(self.data)

        if self.right is not None:
            sorted_list += self.right.sort_ascending()

        return sorted_list

    def sort_descending(self) -> List[Any]:
        sorted_list = []

        if self.data is None:
            return sorted_list

        if self.right is not None:
            sorted_list += self.right.sort_descending()

        sorted_list.append(self.data)

        if self.left is not None:
            sorted_list += self.left.sort_descending()

        return sorted_list

    def search(self, value_to_search: Any) -> bool:
        if self.data == value_to_search:
            return True

        if value_to_search < self.data:
            if self.left is not None:
                return self.left.search(value_to_search)
            return False

        if self.right is not None:
            return self.right.search(value_to_search)
        return False

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def compute_sum(self):
        left_sum = self.left.compute_sum() if self.left is not None else 0
        right_sum = self.right.compute_sum() if self.right is not None else 0
        return left_sum + self.data + right_sum

    def delete_value(self, value_to_delete: Any):
        if value_to_delete < self.data:
            if self.left is not None:
                self.left = self.left.delete_value(value_to_delete)

        elif value_to_delete > self.data:
            if self.right is not None:
                self.right = self.right.delete_value(value_to_delete)
        else:
            # We find the value to delete
            if self.left is None and self.right is None:
                return
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            max_value_from_left_tree_to_duplicate = self.left.find_max()
            self.data = max_value_from_left_tree_to_duplicate
            self.left = self.left.delete_value(max_value_from_left_tree_to_duplicate)

        return self


def build_tree(any_list: List[Any]):
    root_node = any_list[0]
    binary_search_tree = BinarySearchTree(root_node)

    for any_element in any_list[1:]:
        binary_search_tree.add_child_node(any_element)

    return binary_search_tree
