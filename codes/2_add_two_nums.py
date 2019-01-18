# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        listnode = []
        flag = 0
        while l1 or l2 :
            i = l1.val + l2.val + flag
            if i >= 10:
                flag = 1
                i = i - 10
            else:
                flag = 0
            listnode.append(i)
            l1 = l1.next
            l2 = l2.next

        if l1 is None:
            while l2 is not None:
                i = l2.val + flag
                if i >=10:
                    i = i -10
                    flag = 1
                else:
                    flag = 0
                listnode.append(i)
                l2 = l2.next

        if l2 is None:
            while l1 is not None:
                i = l1.val + flag
                if i >= 10:
                    i = i - 10
                    flag = 1
                else:
                    flag = 0
                listnode.append(i)
                l1 = l1.next

        if flag: # 对于5+5这样的实例
            listnode.append(flag)

        return listnode
