import numpy as np
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}  # Create an empty dictionary to store indices

        for index, value in enumerate(nums):
            my_dict[index] = value  # Store each element's value in the dictionary

        index_array = []  # Initialize an empty list to store indices
        index_array_counter = 0  # Initialize a counter to track the number of indices found

        for index_1, i in enumerate(nums):
            for index_2, j in enumerate(nums):
                if i + j == target and index_1 != index_2:  # Check if the pair adds up to the target
                    if i == j:  # If the pair consists of the same element, e.g., (2, 2)
                        for key, value in my_dict.items():
                            if len(index_array) < 2 and value == i:  # Find the indices for both occurrences
                                index_array.append(key)
                    else:  # If the pair consists of different elements, e.g., (1, 3)
                        for key, value in my_dict.items():
                            if len(index_array) < 2 and (i == value or j == value):  # Find the indices
                                index_array.append(key)

        return index_array  # Return the list of indices for the two elements that add up to the target
    # Time Complexity Comment: The nested loops result in a time complexity of O(n^2).


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices = {}  # Create a dictionary to store numbers and their indices

        for index, value in enumerate(nums):
            complement = target - value
            if complement in num_indices:  # Check if the complement is in the dictionary
                return [num_indices[complement], index]  # Return the indices of the pair
            num_indices[value] = index  # Store the current number and its index

        return []  # If no valid pair is found, return an empty list
    # Time Complexity Comment: This code efficiently finds the pair in a single pass through the list, resulting in a
    # time complexity of O(n).


if __name__ == "__main__":
    # Create a Solution instance
    sol = Solution2()

    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print("Test Case 1:", sol.twoSum(nums1, target1))  # Expected output: [0, 1]

    # Test case 2
    nums2 = [3, 2, 4, 10, 5]
    target2 = 9
    print("Test Case 2:", sol.twoSum(nums2, target2))  # Expected output: [1, 2]

    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    print("Test Case 3:", sol.twoSum(nums3, target3))  # Expected output: [0, 1]

    # Add more test cases as needed
