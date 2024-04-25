from collections import defaultdict
from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def amountOfTime(self, root, start):
        """
        :type root: Optional[TreeNode]
        :type start: int
        :rtype: int
        """
        graph = defaultdict(list)
        def dfs (node):
            for child in [node.left, node.right]:
                if child:
                    graph[node.val].append(child.val)
                    graph[child.val].append(node.val)
                    dfs(child)
        dfs(root)

        q = deque([[start, 0]])
        visited = set([start])
        time = 0
        while len(q) > 0:
            nodeVal, time = q.popleft()
            for childVal in graph[nodeVal]:
                if childVal not in visited:
                    q.append([childVal, time+1])
                    visited.add(childVal)
        return time