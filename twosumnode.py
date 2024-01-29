from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Function to traverse a linked list and build an array in reverse order
def traverser(l1: Optional[ListNode], target_array: List) -> None:
    # Recursive approach - O(n) time, O(n) space for call stack
    if l1 is not None:
        # Inserting at the beginning of the list - O(n) time for each insert
        target_array.insert(0, l1.val)
        traverser(l1.next, target_array)


# Function to convert an array of digits into a single number
def converter(array: List[int]):
    # O(m) time complexity, where m is the number of digits
    number = ""
    for index, value in enumerate(array):
        # String concatenation - less efficient due to intermediate string creation
        number = number + str(value)
    return int(number)


# Function to build a linked list from an array
def builder(array: List[int]) -> ListNode:
    # Reverse the array first - O(p) time complexity
    array = list(reversed(array))
    head = ListNode(array[0])
    current = head

    # Build the linked list - O(p) time complexity
    for value in array[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


class Solution:
    # Function to add two numbers represented by linked lists
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> ListNode:
        # Convert linked lists to arrays, reverse them, and then sum - less efficient
        l1_array = []
        l2_array = []
        traverser(l1, l1_array)  # O(n) time and space
        traverser(l2, l2_array)  # O(m) time and space
        l1_np = converter(l1_array)  # O(n) time
        l2_np = converter(l2_array)  # O(m) time

        value = l1_np + l2_np
        Node = builder(list(map(int, str(value))))  # O(p) time for conversion and building

        return Node


class Solution2:
    # More efficient implementation to add two numbers represented by linked lists
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> ListNode:
        # Use a dummy head to simplify edge cases
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        # Single pass through both lists - O(max(n, m)) time, O(1) extra space
        while l1 or l2 or carry:
            # Sum the values from both lists and the carry
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            sum_val = val1 + val2 + carry
            carry = sum_val // 10
            sum_val = sum_val % 10

            # Build the result list directly
            current.next = ListNode(sum_val)
            current = current.next

            # Move to next nodes
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next


# Solution2 is more efficient as it avoids multiple conversions and directly builds the result list in a single pass.


def main():
    # Test cases
    # Test Case 1
    l1 = ListNode(2, ListNode(4, ListNode(3)))  # Represents the number 342
    l2 = ListNode(5, ListNode(6, ListNode(4)))  # Represents the number 465
    # Expected Output: [7, 0, 8]  # Represents the number 807

    # Test Case 2
    l3 = ListNode(0)
    l4 = ListNode(0)
    # Expected Output: [0]  # Represents the number 0

    # Test Case 3
    l5 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(
        9)))))))  # Represents a large number
    l6 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))  # Represents a smaller number
    # Expected Output: [8, 9, 9, 9, 0, 0, 0, 1]  # Represents the sum of the two numbers

    # You can add more test cases as needed
    solution = Solution2()

    # Call the addTwoNumbers function for each test case and print the results
    result1 = solution.addTwoNumbers(l1, l2)

    result2 = solution.addTwoNumbers(l3, l4)

    result3 = solution.addTwoNumbers(l5, l6)

    result1_array = []

    result2_array = []

    result3_array = []

    traverser(result1, result1_array)
    traverser(result2, result2_array)
    traverser(result3, result3_array)

    print("test case 1: ", result1_array)
    print("test case 2: ", result2_array)
    print("test case 3: ", result3_array)


if __name__ == "__main__":
    main()
