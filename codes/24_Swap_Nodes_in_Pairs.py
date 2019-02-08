# Definition for singly-linked list.
import json


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # def swapPairs(self, head: 'ListNode') -> 'ListNode':
    #     root = ListNode(0)
    #     tmp = root
    #     while head:
    #         tmp.next = head.next
    #         tmp = tmp.next
    #         tmp.next = head
    #         head = head.next
    #         tmp = tmp.next
    #         try:
    #             head = head.next
    #         except:
    #             head = head
    #     return root.next
    def swapPairs(self, head):
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next

def stringToIntegerList(input):
    return json.loads(input)


def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            head = stringToListNode(line);

            ret = Solution().swapPairs(head)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
