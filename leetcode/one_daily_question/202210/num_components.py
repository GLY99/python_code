# Definition for singly-linked list.
from typing import Optional, List


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    @staticmethod
    def num_components(self, head: Optional[ListNode], nums: List[int]) -> int:
        """
        给定链表头结点head，该链表上的每个结点都有一个 唯一的整型值 。同时给定列表nums，该列表是上述链表中整型值的一个子集。
        返回列表nums中组件的个数，这里对组件的定义为：链表中一段最长连续结点的值（该值必须在列表nums中）构成的集合。
        :param self:
        :param head:
        :param nums:
        :return:
        """
        node_set = set(nums)
        count = 0
        while head:
            if head.val in node_set:
                head = head.next
                while head and head.val in node_set:
                    head = head.next
                count += 1
            else:
                head = head.next
        return count
