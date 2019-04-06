class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = 0
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s
        longest = s[0]
        while start < len(s) - 1:
            end = start + 1
            while end < len(s):
                flag = True
                for i in range((end - start + 1) // 2):
                    if s[i + start] != s[end - i]:
                        flag = False
                if flag and (end - start) >= len(longest):
                    longest = s[start:end + 1]
                end += 1
            start += 1
        return longest

    def longestPalindrome3(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = 0
        # 使用两个参数来表示当前状态，起始索引和末尾索引
        m = len(s)
        if not m:
            return ""
        if m == 1:
            return s
        state = list([[0] * m for row in range(m)])

        def inits():
            state[0][0] = True
            for i in range(1, m):
                state[i][i] = True
                state[i - 1][i] = s[i] == s[i - 1]

        inits()
        for i in range(m, 0, -1):
            for j in range(i, m - 1):
                state[i - 1][j + 1] = state[i][j] and s[i - 1] == s[j + 1]

        for i in range(m):
            for j in range(i, m):
                if state[i][j] and j - i + 1 > longest:
                    longest = j - i
                    longest_s = s[i:j + 1]

        return longest_s


s = Solution()
print(s.longestPalindrome3("eabcbredj"))
