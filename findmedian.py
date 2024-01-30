import unittest
import math



def find_median_sorted_arrays(nums1, nums2):
    A, B = nums1, nums2
    total = len(A) + len(B)
    partition_half = total // 2

    if len(B) < len(A):
        A, B = B, A

    # Set initial bounds for binary search on the smaller array
    l, r = 0, len(A) - 1  # Get the pointers

    """
     The goal of this function is to find the median of two sorted arrays. Unlike a typical binary search that seeks a specific value, 
     this algorithm uses binary search to find an optimal partition between the two arrays. 

     The optimal partition is defined as one where:
     1. All elements to the left of the partition are less than or equal to all elements to the right.
     2. The combined left and right sides are balanced (either equal in size, or the right side is one larger if the total is odd).

     In each iteration:
     - We take a guess at the partition point in the smaller array (A) by finding its middle index.
     - We calculate the corresponding partition in the larger array (B) to balance the partitions.
     - We then check if the elements around these partitions satisfy the median conditions.

     If the conditions are not met, we adjust the partitions:
     - If the largest element on the left of A's partition is greater than the smallest on the right of B's partition, 
       it indicates our partition in A is too far to the right. Hence, we move the partition in A leftwards (reduce r).
     - Conversely, if the largest element on the left of B's partition is greater than the smallest on the right of A's partition,
       we need to move the partition in A rightwards (increase l).

     Once a valid partition is found, the median is determined based on whether the total number of elements is odd or even:
     - If even, the median is the average of the largest element on the left and smallest on the right.
     - If odd, the median is the smaller of the two elements immediately to the right of the partitions.
     """

    while True:
        index_A_pointer = (l + r) // 2  # We take a guess by finding the middle index
        print(l,r)

        index_B_pointer = partition_half - (
                    index_A_pointer + 1) - 1  # We do this to find how much numbers the a pointer holds then we convert it into an index b pointer

        Aleft = A[index_A_pointer] if index_A_pointer >= 0 else -math.inf  # Get the left value of the partition
        Aright = A[index_A_pointer + 1] if (index_A_pointer + 1) < len(
            A) else math.inf  # Get the right value of the partition
        Bleft = B[index_B_pointer] if index_B_pointer >= 0 else -math.inf  # Get the left value of the partition
        Bright = B[index_B_pointer + 1] if (index_B_pointer + 1) < len(
            B) else math.inf  # Get the right value of the partition

        # Check if the partition is correct oterwise we mode the median to hone in ont he correct value
        if Aleft <= Bright and Bleft <= Aright:
            if total % 2 == 0:
                median = (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                return median
            else:
                median = min(Aright, Bright)
                return median
        if Aleft > Bright:
            r = index_A_pointer - 1
        else:
            l = index_A_pointer + 1


class TestFindMedianSortedArrays(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(find_median_sorted_arrays([1, 5, 7 , 7, 8,8 ,8, 9, 13, 17, 21, 25, 29, 33, 37], [2, 6, 10, 14, 18, 22, 26, 30, 34, 38]), 14)
        self.assertEqual(find_median_sorted_arrays([1, 2], [3, 4]), 2.5)

    def test_empty_array(self):
        self.assertEqual(find_median_sorted_arrays([], [1]), 1.0)
        self.assertEqual(find_median_sorted_arrays([2], []), 2.0)

    def test_single_element_arrays(self):
        self.assertEqual(find_median_sorted_arrays([1], [2]), 1.5)
        self.assertEqual(find_median_sorted_arrays([2], [1]), 1.5)

    def test_uneven_arrays(self):
        self.assertEqual(find_median_sorted_arrays([1, 2], [3, 4, 5]), 3.0)
        self.assertEqual(find_median_sorted_arrays([1, 3, 5], [2, 4]), 3.0)

    def test_large_numbers(self):
        self.assertEqual(find_median_sorted_arrays([1000000], [1000001]), 1000000.5)

    def test_negative_numbers(self):
        self.assertEqual(find_median_sorted_arrays([-5, -3, -1], [-2, 0, 2]), -1.5)

    def test_combined(self):
        self.assertEqual(find_median_sorted_arrays([-1, 0, 1], [100, 1000, 10000]), 50.5)


if __name__ == '__main__':
    unittest.main()
