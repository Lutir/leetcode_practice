'''
https://leetcode.com/problems/two-sum/description/
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''
import unittest
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    for i in range(n):
        element = nums[i]
        for j in range(i + 1, n):
            if nums[j] == target - element:
                return [i, j]
    return nums

class TestTwoSum(unittest.TestCase):
    def test_twoSum_example1(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        self.assertEqual(twoSum(nums, target), expected)

    def test_twoSum_example2(self):
        nums = [3, 2, 4]
        target = 6
        expected = [1, 2]
        self.assertEqual(twoSum(nums, target), expected)

    def test_twoSum_no_solution(self):
        nums = [1, 2, 3, 4]
        target = 10
        expected = nums
        self.assertEqual(twoSum(nums, target), expected)

    def test_twoSum_single_element(self):
        nums = [5]
        target = 10
        expected = nums
        self.assertEqual(twoSum(nums, target), expected)

    def test_twoSum_empty_list(self):
        nums = []
        target = 10
        expected = nums
        self.assertEqual(twoSum(nums, target), expected)

    def test_twoSum_duplicate_elements(self):
        nums = [1, 2, 3, 3]
        target = 6
        expected = [2, 3]
        self.assertEqual(twoSum(nums, target), expected)

    def test_twoSum_negative_numbers(self):
        nums = [-3, 4, 3, 90]
        target = 0
        expected = [0, 2]
        self.assertEqual(twoSum(nums, target), expected)

if __name__ == '__main__':
    unittest.main()

