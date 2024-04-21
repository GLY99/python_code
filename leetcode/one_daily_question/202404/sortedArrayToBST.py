# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.helper(nums, 0, len(nums) - 1)
    
    def helper(self, nums, left, right):
        """
        helper
        """
        if left > right:
            return None
        mid = (left + right) / 2
        root = TreeNode(val=nums[mid])
        root.left = self.helper(nums, left, mid - 1)
        root.right = self.helper(nums, mid + 1, right)
        return root

        