import unittest


class IsNotANumberError(Exception):
    def __init__(self, message="The value provided is not a number"):
        self.message = message
        super().__init__(self.message)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def push(self, value):

        if not isinstance(value, (int, float, complex)):
            raise IsNotANumberError(f"{value} is not a number")

        node = Node(value)

        if self.bottom is None:
            self.bottom = node
            self.top = node
            self.length +=1
        else:
            node.next = self.top
            self.top = node
            self.length += 1

    def pop(self):
        new_node_on_top = self.top.next

        if new_node_on_top is None:
            self.bottom = None
            self.top = None
            self.length -= 1
            return

        else:
            self.top = new_node_on_top
            self.length -= 1

    def peek(self):
        return self.top


# Your exception, Node, and Stack classes go here

class TestStack(unittest.TestCase):

    def test_push_and_peek(self):
        stack = Stack()
        stack.push(5)
        self.assertEqual(stack.peek().value, 5)
        stack.push(10)
        self.assertEqual(stack.peek().value, 10)

    def test_pop(self):
        stack = Stack()
        stack.push(5)
        stack.push(10)
        stack.pop()
        self.assertEqual(stack.peek().value, 5)
        stack.pop()
        self.assertIsNone(stack.peek())

    def test_is_not_a_number_error(self):
        stack = Stack()
        with self.assertRaises(IsNotANumberError):
            stack.push("not a number")


if __name__ == '__main__':
    unittest.main()
