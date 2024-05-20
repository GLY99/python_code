class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        desc = ("Gold Medal", "Silver Medal", "Bronze Medal")
        mapping = {}
        for idx, s in enumerate(score):
            mapping[s] = idx
        score = sorted(score, key=lambda x: -x)
        res = [0] * len(score)
        for i, s in enumerate(score):
            if i < 3:
                res[mapping[s]] = desc[i]
            else:
                res[mapping[s]] = str(i + 1)
        return res