import unittest

import unittest

class SimpleHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def set(self, key, value):
        index = self._hash(key)
        # Iterate through the list at the index to find if the key exists
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)  # Update value if key found
                return
        self.table[index].append((key, value))  # Append new key-value pair if key not found

    def get(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v  # Return value if key found
        return None  # Return None if key not found




class TestSimpleHashTable(unittest.TestCase):

    def test_set(self):
        hash_table = SimpleHashTable(10)
        hash_table.set("naam", "arthike")
        # Test will be expanded after implementation

    def test_get(self):
        hash_table = SimpleHashTable(10)
        hash_table.set("achternaam", "schoolklaar")
        result = hash_table.get("achternaam")
        # Test will be expanded after implementation


if __name__ == '__main__':
    unittest.main()
