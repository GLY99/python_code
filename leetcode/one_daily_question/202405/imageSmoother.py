class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        m = len(img)
        n = len(img[0])
        for i, _ in enumerate(img):
            ans.append([])
            for j, _ in enumerate(img[i]):
                s, num = 0, 0
                for row in img[max(i - 1, 0): min(i + 2, m)]:
                    for v in row[max(j - 1, 0): min(j + 2, n)]:
                        s += v
                        num += 1
                ans[i].append(s / num)
        return ans