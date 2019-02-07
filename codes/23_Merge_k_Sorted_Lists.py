# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        lens = len(lists)
        if not lens:
            return []
        elif lens == 1:
            return lists[0]
        else:
            return self.devide(lists, 0, lens - 1)

    def devide(self, lists, l_p, r_p):
        if l_p == r_p:
            return lists[l_p]
        else:
            mid = (l_p + r_p) // 2
            left = self.devide(lists, l_p, mid)
            right = self.devide(lists, mid + 1, r_p)
            return self.merge2Lists(left, right)

    def merge2Lists(self, list1, list2):
        root = ListNode(0)
        tmp = root
        while list1 and list2:
            if list1.val > list2.val:
                tmp.next = list2
                list2 = list2.next
                tmp = tmp.next
            else:
                tmp.next = list1
                list1 = list1.next
                tmp = tmp.next
        if list1:
            tmp.next = list1
        if list2:
            tmp.next = list2
        return root.next
