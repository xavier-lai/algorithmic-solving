# algorithmic-solving

Algorithmic solving in python

## I - Data Structure

### HashTable

Hashtable is already implemented in python with Dict. Insert, Get or Delete operation inside a HashTable with no collision is a complexity of O(1). If there are collision it will depends on the quality of the hash functions.

```python
from src.data_structure import HashTable

if __name__ == "__main__":
    hash_table = HashTable(max_length=10)
    hash_table.set_value("my_key", 1245)
    hash_table.set_value("other key", 1)
    hash_table.set_value("batman", 26)
    print(hash_table.hash_list)
    hash_table.set_value("my_key", 80)
    hash_table.delete_key("my_key")
    print(hash_table.hash_list)
```

### LinkedList

LinkedList can set the complexity to O(1) when one want to insert/delete at the begining of an array. Moreover it will reserve less space in RAM.

```python
from src.data_structure import LinkedList

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_at_begining(5)
    linked_list.insert_at_begining(8)
    linked_list.insert_at_begining(1023)
    linked_list.insert_at_end(1023)
    linked_list.insert_values([1, 5, 6, 7])
    linked_list.insert_values([0, 0, 0], insert_at_the_end=False)
    linked_list.remove_at(3)
    linked_list.show()
    linked_list.insert_at(1000000, linked_list.get_length())
    linked_list.show()
    linked_list.reverse()
    linked_list.show()
    linked_list.reverse_recursive(linked_list.head)
    linked_list.show()
```

### Binary Search Tree

Binary search tree is a general tree where each node has at most 2 child nodes. All values lower than current node value are in the sub-left tree and all values greater than the current node value are in the sub-right tree.

The time complexity of searching and sorting with a BinarySearchTree is O(log(n))

```python
from src.data_structure import build_tree

if __name__ == "__main__":
    int_list = [100, 50, 150, 200, 1000, 20, 60, 45, 5, 25, 6]
    binary_search_tree = build_tree(int_list)
    print(binary_search_tree.sort_ascending())
    print(binary_search_tree.search(2))
    print(binary_search_tree.search(1023))
    print(binary_search_tree.find_max())
    print(binary_search_tree.find_min())
    print(binary_search_tree.compute_sum())
    print(binary_search_tree.sort_descending())
    print(binary_search_tree.sort_ascending())
    binary_search_tree.delete_value(50)
    print(binary_search_tree.sort_ascending())
```

## II - Search

### Binary Search

Binary search search in a O(log(n)) time complexity in an array. The array must be sorted

```python
from src.search import binary_search, binary_search_recursive, search_all_occurances

if __name__ == "__main__":
    any_list = sorted([0, 5, 410, 58, 58, 58, 65, 12, 0, 112, 53, 120, 568, 5])
    print(any_list)
    print(binary_search(120, any_list))
    index = binary_search_recursive(
        120, any_list, lower_bound_index=0, upper_bound_index=len(any_list)
    )
    print(f"Found at {index}")
    print(search_all_occurances(58, any_list))
```

## III - Sort

### Bubble sort

Compare each value and permute the greteast element with the next one until all elements are sorted. The complexity is around O(n²)

```python
from src.sort import bubble_sort

if __name__ == "__main__":
    any_int_list = [10, 25, 0, 4, 3, 102, 356, 1000, 3, 0, 0, 5]
    already_sorted_list = sorted(any_int_list)
    print(bubble_sort(any_int_list))
    print(bubble_sort(already_sorted_list))
```

### Quick sort

Sort by sorting partitions. The time complexity is at the worst O(n²) and at the best O(nlog(n)).

```python
from src.sort import quick_sort

if __name__ == "__main__":
    any_int_list = [0, 20, 1, 542, 3, 6, 7, 89, 2, 0, 0, 12, 6]
    print(quick_sort(any_int_list))
```
