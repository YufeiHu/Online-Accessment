"""
@author: Yufei Hu
@date: 01/23/2019
@source: Leetcode-21
"""

class Solution:
    def mergeTwoLists(self, l1, l2):
        pre_head = ListNode(0)
        ptr = pre_head
        while l1 and l2:
            if l1.val > l2.val:
                ptr.next = l2
                ptr = ptr.next
                l2 = l2.next
            else:
                ptr.next = l1
                ptr = ptr.next
                l1 = l1.next
        if l1: ptr.next = l1
        if l2: ptr.next = l2
        return pre_head.next
