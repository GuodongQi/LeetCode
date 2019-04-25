class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        xlist = []
        y = 0
        isneg = 0
        ground = - 2 ** 31
        flor = -ground - 1
        if x < 0:
            x = -x
            isneg = 1
        while x:
            n = x % 10
            x = x // 10
            xlist.append(n)
        lens = len(xlist)
        for i, item in enumerate(xlist):
            y = y + item * 10 ** (lens - i - 1)
        if isneg:
            y = -y
        if y < ground or y > flor:
            y = 0
        return y

s = Solution()
print(s.reverse(1534236469))
