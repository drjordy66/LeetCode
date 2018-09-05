# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_unlinked = []
        l2_unlinked = []
        while l1 != None:
            l1_unlinked.append(l1.val)
            l1 = l1.next
        while l2 != None:
            l2_unlinked.append(l2.val)
            l2 = l2.next
        return sorted(l1_unlinked + l2_unlinked)
