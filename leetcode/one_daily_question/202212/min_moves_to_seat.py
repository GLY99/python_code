from typing import List


class Solution(object):
    def min_moves_to_seat(self, seats: List[int], students: List[int]) -> int:
        """
        min moves to seat
        :param seats:
        :param students:
        :return:
        """
        seats.sort()
        students.sort()
        return sum(abs(a - b) for a, b in zip(students, seats))