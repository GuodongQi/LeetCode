import json


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: 'ListNode', k: 'int') -> 'ListNode':
        i = 0
        root = ListNode(0)
        root_tmp = root
        part_head = ListNode(0)
        tmp = part_head
        while i < k:
            if head is None:
                root_tmp.next = part_head.next
                break
            else:
                tmp.next = head
                head = head.next
                tmp = tmp.next
                i += 1
                if i == k:
                    tmp.next = None
                    root_tmp.next = self.reverseK(part_head.next, k)
                    part_head = ListNode(0)
                    tmp = part_head
                    i = 0
                    while root_tmp.next is not None:
                        root_tmp = root_tmp.next
        return root.next

    def reverseK(self, head, k):
        root = ListNode(0)
        tmp = root
        lists = []
        for i in range(k):
            if head is None:
                break
            lists.append(head.val)
            head = head.next
        lists = lists[::-1]
        for item in lists:
            tmp.next = ListNode(item)
            tmp = tmp.next
        tmp.next = head
        return root.next


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
            line = next(lines)
            k = int(line);

            ret = Solution().reverseKGroup(head, k)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
