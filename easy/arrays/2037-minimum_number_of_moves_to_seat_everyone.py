'''
https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/description/?envType=daily-question&envId=2024-06-13

There are n seats and n students in a room. You are given an array seats of length n, where seats[i] is the position of the ith seat. You are also given the array students of length n, where students[j] is the position of the jth student.

You may perform the following move any number of times:

    Increase or decrease the position of the ith student by 1 (i.e., moving the ith student from position x to x + 1 or x - 1)

Return the minimum number of moves required to move each student to a seat such that no two students are in the same seat.

Note that there may be multiple seats or students in the same position at the beginning.
'''
import unittest
from typing import List

def minMovesToSeat(seats: List[int], students: List[int]) -> int:
    seats.sort()
    students.sort()

    moves = 0
    for i in range(len(students)):
        moves += abs(seats[i] - students[i])

    return moves

class TestMinMovesToSeat(unittest.TestCase):
    def test_example1(self):
        seats = [3, 1, 5]
        students = [2, 7, 4]
        expected = 4
        self.assertEqual(minMovesToSeat(seats, students), expected)

    def test_example2(self):
        seats = [4, 1, 5, 9]
        students = [1, 3, 2, 6]
        expected = 7
        self.assertEqual(minMovesToSeat(seats, students), expected)

    def test_empty_lists(self):
        seats = []
        students = []
        expected = 0
        self.assertEqual(minMovesToSeat(seats, students), expected)

    def test_single_element(self):
        seats = [5]
        students = [5]
        expected = 0
        self.assertEqual(minMovesToSeat(seats, students), expected)

    def test_duplicate_elements(self):
        seats = [1, 1, 3, 3]
        students = [3, 1, 1, 3]
        expected = 0
        self.assertEqual(minMovesToSeat(seats, students), expected)

    def test_large_input(self):
        seats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        students = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        expected = 0
        self.assertEqual(minMovesToSeat(seats, students), expected)

if __name__ == '__main__':
    unittest.main()

