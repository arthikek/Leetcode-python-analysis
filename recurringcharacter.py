import unittest


# Replace this with your own implementation of find_first_recurring_number
def find_first_recurring_number(arr):
    # We will scan through the array and build a hashmap.
    # We will check if the number is already present in the hashmap as a key
    # We use a hashmap because we need to have a qucik lookup

    Hashmap = {}

    if Hashmap is None:
        return None

    for index, value in enumerate(arr):
        if Hashmap.get(value) is not None:
            return value


        else:
            Hashmap[value] = index


class TestFindFirstRecurringNumber(unittest.TestCase):

    def test_first_recurring_number_found(self):
        arr = [2, 5, 1, 2, 3, 5, 1, 2, 4]
        result = find_first_recurring_number(arr)
        self.assertEqual(result, 2)

    def test_no_recurring_number_found(self):
        arr = [1, 2, 3, 4, 5]
        result = find_first_recurring_number(arr)
        self.assertIsNone(result)

    def test_empty_array(self):
        arr = []
        result = find_first_recurring_number(arr)
        self.assertIsNone(result)

    def test_recurring_number_at_start(self):
        arr = [2, 2, 3, 4, 5]
        result = find_first_recurring_number(arr)
        self.assertEqual(result, 2)

    def test_recurring_number_at_end(self):
        arr = [1, 2, 3, 4, 5, 5]
        result = find_first_recurring_number(arr)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
