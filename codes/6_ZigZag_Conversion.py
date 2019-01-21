class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        m = len(s)
        v = 2 * numRows - 1
        v_nums = m // v + 1
        cols = v_nums * (numRows - 1)
        # matrix = [[0] * cols for row in range(numRows)]
        matrix = []
        v_num = 0

        for i in range(m):
            v_num = i // v
            bias = i % v
            matrix.append()

s = Solution()
s.convert("PAYPALISHIRING", 4)
