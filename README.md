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
