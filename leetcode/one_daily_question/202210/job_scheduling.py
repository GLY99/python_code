from typing import List


class Work(object):
    """
    work class
    """
    def __init__(self, start_time: int, end_time: int, profit: int):
        self.start_time = start_time
        self.end_time = end_time
        self.profit = profit

    def __repr__(self):
        return f"[{self.start_time}, {self.end_time}, {self.profit}]"


class Solution:
    @staticmethod
    def job_scheduling(start_time: List[int], end_time: List[int], profit: List[int]) -> int:
        """
        :param start_time:
        :param end_time:
        :param profit:
        :return:
        """
        length = len(profit)
        work_list = [Work(start_time[i], end_time[i], profit[i]) for i in range(length)]
        work_list = sorted(work_list, key=lambda x: x.end_time)
        dp_arr = [0] * (length + 1)
        for i in range(1, length + 1):
            pre_finish_work = 0
            j = i - 1
            while j >= 0:
                if work_list[j].end_time <= work_list[i - 1].start_time:
                    pre_finish_work = j + 1
                    break
                j -= 1
            dp_arr[i] = max(dp_arr[i - 1], dp_arr[pre_finish_work] + work_list[i - 1].profit)
        return dp_arr[-1]


if __name__ == "__main__":
    sol = Solution()
    startTime = [1, 2, 3, 3]
    endTime = [3, 4, 5, 6]
    profit = [50,10,40,70]
    print(sol.job_scheduling(startTime, endTime, profit))