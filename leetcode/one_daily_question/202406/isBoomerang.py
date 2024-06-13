class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        x1, y1 = points[0][0], points[0][1]
        x2, y2 = points[1][0], points[1][1]
        x3, y3 = points[2][0], points[2][1]
        if x1 == x2 and y1 == y2 or x1 == x3 and y1 == y3 or x2 == x3 and y2 == y3:
            return False
        else:
            # Ax + By + C == 0证明点在线上
            A = y1 - y2
            B = x2 - x1
            C = x1*y2 - x2*y1
            if A*x3+B*y3+C == 0:
                return False
            else:
                return True