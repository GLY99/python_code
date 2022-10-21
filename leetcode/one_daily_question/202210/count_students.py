from typing import List


class Solution:
    @staticmethod
    def count_students(students: List[int], sandwiches: List[int]) -> int:
        """
        :param students:
        :param sandwiches:
        :return:
        """
        for sandwiche in sandwiches:
            if sandwiche in students:
                students.remove(sandwiche)
            else:
                break
        return len(students)

    @staticmethod
    def count_students(students: List[int], sandwiches: List[int]) -> int:
        """
        :param students:
        :param sandwiches:
        :return:
        """
        while len(students) != 0 and len(sandwiches) != 0:
            student = students.pop(0)
            if student == sandwiches[0]:
                sandwiches.pop(0)
            else:
                students.append(student)
            if len(sandwiches) != 0 and sandwiches[0] not in students:
                break
        return len(students)


if __name__ == "__main__":
    sol = Solution()
    students = [1, 1, 1, 0, 0, 1]
    sandwiches = [1, 0, 0, 0, 1, 1]
    print(sol.count_students(students, sandwiches))