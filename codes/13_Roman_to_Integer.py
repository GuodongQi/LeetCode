class Solution:
    def romanToInt(self, s):
        """:type s: str
        :rtype: int
        """
        symbols = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
        nums = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        out = 0
        m = len(s)
        i = 0
        while i < m:
            if i + 1 < m and s[i:i + 2] in symbols:
                out += nums[symbols.index(s[i:i + 2])]
                i += 2
            elif s[i] in symbols:
                out += nums[symbols.index(s[i])]
                i += 1
            else:
                i += 1
        return out


s = Solution()
print(s.romanToInt("MCMXCIV"))
print(s.romanToInt("LVIII"))
