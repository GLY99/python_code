class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        idx = start
        length = len(distance)
        distance1 = 0
        while idx % length != destination:
            distance1 += distance[idx % length]
            idx += 1
        distance2 = 0
        idx = destination
        while idx % length != start:
            distance2 += distance[idx % length]
            idx += 1
        return min(distance1, distance2)