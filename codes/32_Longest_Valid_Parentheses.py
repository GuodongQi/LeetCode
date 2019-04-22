class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l = len(s)
        left, right = 0, 0
        max_len = 0
        for char in s:
            if char == '(':
                left += 1
            else:
                right += 1
            if left == right:
                if max_len < left * 2:
                    max_len = left * 2
            elif left <= right:
                right = 0
                left = 0

        right = 0
        left = 0
        for char in s[::-1]:
            if char == '(':
                left += 1
            else:
                right += 1
            if left == right:
                if max_len < left * 2:
                    max_len = left * 2
            elif left >= right:
                right = 0
                left = 0
        return max_len


s = Solution()
print(s.longestValidParentheses('())((())'))
