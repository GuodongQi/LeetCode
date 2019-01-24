class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbols = ["I", "IV", "V", "IX", "X", "XL", "L", "XL", "XC", "C", "CD", "D", "CM", "M"]
        nums = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]

        for i in range(len(s)):



s = Solution()
print(s.romanToInt("1994"))

