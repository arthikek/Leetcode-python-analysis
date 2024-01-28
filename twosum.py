import numpy as np
from typing import List


class Solution:
    def twosum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for index, value in enumerate(nums):
            my_dict[index] = value

        index_array = []
        index_array_counter = 0

        for index_1, i in enumerate(nums):
            for index_2, j in enumerate(nums):
                if i + j == target and index_1 != index_2:
                    if i == j:
                        for key, value in my_dict.items():
                            if len(index_array) < 2 and value == i:
                                index_array.append(key)
                    else:
                        for key, value in my_dict.items():
                            if len(index_array) < 2 and (i == value or j == value):
                                index_array.append(key)

        return index_array





class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices = {}

        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_indices:
                return [num_indices[complement], index]
            num_indices[num] = index

        return []



if __name__ == "__main__":
    # Create a Solution instance
    sol = Solution2()

    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print("Test Case 1:", sol.twosum(nums1, target1))  # Expected output: [0, 1]

    # Test case 2
    nums2 = [3, 2, 4, 10, 5]
    target2 = 9
    print("Test Case 2:", sol.twosum(nums2, target2))  # Expected output: [1, 2]

    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    print("Test Case 3:", sol.twosum(nums3, target3))  # Expected output: [0, 1]

    # Add more test cases as needed
