# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        lists = []
        while head is not None:
            lists.append(head.val)
            head = head.next

        root = ListNode(0)
        ptr = root
        for i, item in enumerate(lists):
            if i == len(lists) - n:
                continue
            ptr.next = ListNode(item)
            ptr = ptr.next

        return root.next