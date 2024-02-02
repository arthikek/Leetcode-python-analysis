import unittest
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedListClass:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            tail = self.tail
            tail.next = new_node
            new_node.prev = tail
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            head = self.head
            head.prev = new_node
            new_node.next = head
            self.head = new_node
        self.length += 1
    def insert(self, value, index):
        current_node = self.head
        before_node = 0

        for i in range(index):
            before_node = current_node
            current_node = current_node.next

        new_node = Node(value)
        before_node.next = new_node
        new_node.prev = before_node
        new_node.next = current_node
        current_node.prev = new_node
        self.length += 1

    def delete(self, index):
        current_node = self.head
        before_node = 0

        for i in range(index):
            before_node = current_node
            current_node = current_node.next

        if current_node is not None:
            next_node = current_node.next
            if next_node is not None:
                before_node.next = next_node
                next_node.prev = before_node
                self.length -= 1
            else:
                before_node.next = None
                self.length -= 1


def linked_list_to_list(linked_list, forward=True):
    output = []
    current_node = linked_list.head if forward else linked_list.tail
    while current_node:
        output.append(current_node.value)
        current_node = current_node.next if forward else current_node.prev
    return output


class TestLinkedListClass(unittest.TestCase):

    def setUp(self):
        self.ll = LinkedListClass()

    def linked_list_to_list(self, linked_list):
        output = []
        current_node = linked_list.head
        while current_node:
            output.append(current_node.value)
            current_node = current_node.next
        return output

    def test_append(self):
        self.ll.append(1)
        self.assertEqual(self.ll.tail.value, 1)
        self.assertEqual(self.ll.length, 1)
        self.assertEqual(linked_list_to_list(self.ll), [1])

        self.ll.append(2)
        self.assertEqual(self.ll.tail.value, 2)
        self.assertEqual(self.ll.length, 2)
        self.assertEqual(linked_list_to_list(self.ll), [1, 2])

    def test_prepend(self):
        self.ll.prepend(1)
        self.assertEqual(self.ll.head.value, 1)
        self.assertEqual(self.ll.length, 1)
        self.assertEqual(linked_list_to_list(self.ll), [1])

        self.ll.prepend(0)
        self.assertEqual(self.ll.head.value, 0)
        self.assertEqual(self.ll.length, 2)
        self.assertEqual(linked_list_to_list(self.ll), [0, 1])

    def test_insert(self):
        self.ll.append(1)
        self.ll.append(3)
        self.ll.insert(2, 1)  # Assuming the insert method signature is insert(value, position)
        self.assertEqual(self.ll.length, 3)
        self.assertEqual(linked_list_to_list(self.ll), [1, 2, 3])

    def test_delete(self):
        self.ll.append(1)
        self.ll.append(2)
        self.ll.append(3)
        self.ll.delete(1)
        self.assertEqual(self.ll.length, 2)
        self.assertEqual(linked_list_to_list(self.ll), [1, 3])

    def test_backward_traversal(self):
        # Test backward traversal of the list
        self.ll.append(1)
        self.ll.append(2)
        self.ll.append(3)

        # Forward traversal (as a reference)
        forward_list = linked_list_to_list(self.ll, forward=True)

        # Backward traversal
        backward_list = linked_list_to_list(self.ll, forward=False)

        # Check that the backward traversal is correct
        self.assertEqual(backward_list, list(reversed(forward_list)))
if __name__ == "__main__":
    unittest.main()
