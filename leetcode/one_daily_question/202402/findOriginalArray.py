class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        changed = sorted(changed)
        myMap = {}
        for num in changed:
            if num in myMap:
                myMap[num] += 1
            else:
                myMap[num] = 1
        res = []
        for num in changed:
            if myMap[num] == 0:
                continue
            myMap[num] -= 1
            if num * 2 not in myMap or myMap[num * 2] == 0:
                return []
            myMap[num * 2] -= 1
            res.append(num)
        return res
    