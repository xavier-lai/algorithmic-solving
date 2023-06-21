from typing import Any, List, Optional

from ..decorators import time_it


class LinkedList:
    def __init__(self):
        self.head = None

    def show(self):
        if self.head is None:
            print("LinkedList is empty.")

        current_node = self.head
        show_str = ""
        while current_node is not None:
            show_str += f"{current_node.data}-->"
            current_node = current_node.next
        print(show_str)

    def insert_at_begining(self, data: Any):
        first_node = Node(data, self.head)
        self.head = first_node

    def insert_at_end(self, data: Any):
        end_node = Node(data)
        current_node = self.head

        if current_node is None:
            self.head = end_node
            return

        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = end_node

    def insert_values(self, data_list: List[Any], insert_at_the_end: bool = True):
        for data in data_list:
            if insert_at_the_end:
                self.insert_at_end(data)
            else:
                self.insert_at_begining(data)

    def get_length(self) -> int:
        node_counter = 0
        current_node = self.head

        if current_node is None:
            return node_counter

        while current_node.next is not None:
            node_counter += 1
            current_node = current_node.next
        return node_counter + 1

    def insert_at(self, data: Any, index_to_insert: int):
        if index_to_insert < 0 or index_to_insert > self.get_length():
            raise IndexError("Index can't be reached")

        if index_to_insert == 0:
            self.insert_at_begining(data)
            return

        current_node = self.head
        current_index = 0
        while current_node is not None:
            if current_index == index_to_insert - 1:
                node_to_insert = Node(data, next=current_node.next)
                current_node.next = node_to_insert
                break
            current_node = current_node.next
            current_index += 1

    def remove_at(self, index_to_remove: int):
        if index_to_remove < 0 or index_to_remove > self.get_length():
            raise IndexError("Index can't be reached")

        current_node = self.head

        if index_to_remove == 0:
            current_node = current_node.next

        current_index = 0
        while current_node is not None:
            if current_index == index_to_remove - 1:
                current_node.next = current_node.next.next
                break
            current_node = current_node.next
            current_index += 1
        current_node = current_node.next  # in case it's the last index

    @time_it
    def reverse(self):
        if self.head is None:
            return

        previous_node = None
        current_node = self.head
        while current_node is not None:
            tmp_next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = tmp_next_node

        self.head = previous_node

    @time_it
    def reverse_recursive(self, current_node, previous_node=None):
        if current_node is None:
            self.head = previous_node
            return

        next_node = current_node.next
        current_node.next = previous_node
        self.reverse_recursive(next_node, current_node)


class Node:
    def __init__(self, data: Optional[Any] = None, next=None):
        self.data = data
        self.next = next
