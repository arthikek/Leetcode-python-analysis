import unittest


class Node:
    """A Node of the LinkedList."""

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedListClass:
    """LinkedListClass to be implemented."""

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:  # If the list is empty
            self.head = new_node
            self.tail = new_node
        else:
            tail = self.tail
            tail.next = new_node
            self.tail = new_node

        self.length += 1  # Increment the length for both empty and non-empty list cases

    def prepend(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.length += 1

    def insert(self, value, index):
        current_node = self.head
        before_node = 0

        for i in range(index):
            before_node = current_node
            current_node = current_node.next

        new_Node = Node(value)
        before_node.next = new_Node
        new_Node.next = current_node
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
                self.length -= 1
            else:
                before_node.next = None
                self.tail = before_node
                self.length -= 1
        else:
            Node = before_node
            Node.next = None
            self.length -= 1


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
        self.assertEqual(self.linked_list_to_list(self.ll), [1])

        self.ll.append(2)
        self.assertEqual(self.ll.tail.value, 2)
        self.assertEqual(self.ll.length, 2)
        self.assertEqual(self.linked_list_to_list(self.ll), [1, 2])

    def test_prepend(self):
        self.ll.prepend(1)
        self.assertEqual(self.ll.head.value, 1)
        self.assertEqual(self.ll.length, 1)
        self.assertEqual(self.linked_list_to_list(self.ll), [1])

        self.ll.prepend(0)
        self.assertEqual(self.ll.head.value, 0)
        self.assertEqual(self.ll.length, 2)
        self.assertEqual(self.linked_list_to_list(self.ll), [0, 1])

    def test_insert(self):
        self.ll.append(1)
        self.ll.append(3)
        self.ll.insert(2, 1)  # Assuming the insert method signature is insert(value, position)
        self.assertEqual(self.ll.length, 3)
        self.assertEqual(self.linked_list_to_list(self.ll), [1, 2, 3])

if __name__ == "__main__":
    unittest.main()
