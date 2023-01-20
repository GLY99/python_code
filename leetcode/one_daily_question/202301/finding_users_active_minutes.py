from typing import List
from collections import defaultdict


class Solution:
    def finding_users_active_minutes(self, logs: List[List[int]], k: int) -> List[int]:
        """
        finding user activate minutes
        :param logs:
        :param k:
        :return:
        """
        user_map = defaultdict(set)
        for user_id, minute in logs:
            user_map[user_id].add(minute)
        res = [0] * k
        for val in user_map.values():
            res[len(val) - 1] += 1
        return res


if __name__ == "__main__":
    """
    main
    """
    sol = Solution()
    logs = [[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]]
    k = 5
    print(sol.finding_users_active_minutes(logs, k))