class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return [""]
        if n > 0:
            ans = []
            for i in range(n):
                for left in self.generateParenthesis(i):
                    for right in self.generateParenthesis(n - 1 - i):
                        ans.append('({}){}'.format(left, right))

            return ans


s = Solution()
print(s.generateParenthesis(3))
