'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
'''
import unittest
from typing import List

def plusOne(digits: List[int]) -> List[int]:
    for i in reversed(range(len(digits))):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            return digits
    
    return [1] + digits

class TestPlusOne(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(plusOne([1, 2, 3]), [1, 2, 4])
        self.assertEqual(plusOne([4, 3, 2, 1]), [4, 3, 2, 2])

    def test_all_nines(self):
        self.assertEqual(plusOne([9, 9, 9]), [1, 0, 0, 0])
        self.assertEqual(plusOne([7, 9, 9]), [8, 0, 0])


    def test_single_digit(self):
        self.assertEqual(plusOne([9]), [1, 0])
        self.assertEqual(plusOne([0]), [1])

if __name__ == '__main__':
    unittest.main()
