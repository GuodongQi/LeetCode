class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # if not len(s):
        #     return s

        m = len(s)  # 字符串长度
        if numRows == 1 or numRows >=m:
            return s
        v = 2 * numRows - 2  # 一个v字结构有多少个字符
        v_nums = m // v + 1  # 总共有多少个v结构
        cols = v_nums * (numRows - 1)  # 计算列数
        matrix = list([[0] * cols for row in range(numRows)])  # 构建矩阵
        k = 0
        new_str = []
        for i in range(v_nums):  # 第i个v结构
            for j in range(numRows):  # 第i个v结构的第j行
                if k == m:
                    break
                matrix[j][i * (numRows - 1)] = s[k]
                k += 1
            for j in range(1, numRows-1):
                if k == m:
                    break
                matrix[numRows - j - 1][i * (numRows - 1) + j] = s[k]
                k += 1

        for ii in range(numRows):
            for jj in range(cols):
                if matrix[ii][jj]:
                    new_str.append(matrix[ii][jj])
        return "".join(new_str)

    def convert2(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # 暴力循环
        # if not len(s):
        #     return s
        if numRows == 1 or numRows >= len(s):
            return s
        m = len(s)  # 字符串长度
        v = 2 * numRows - 2  # 一个v字结构有多少个字符
        v_nums = m // v + 1  # 总共有多少个v结构
        rn = list(range(0, numRows - 1)) + list(range(numRows - 1, 0, -1))
        z = [""] * numRows
        cols = v_nums * (numRows - 1)  # 计算列数
        # matrix = list([[0] * cols for row in range(numRows)])  # 构建矩阵
        k = 0
        new_str = []
        for i in range(v_nums):  # 第i个v结构
            for j in range(v):  # 第i个v结构的第j个字符
                z[rn[j]] += s[k]
                if k == m-1:
                    return "".join(z)
                else:
                    k += 1


s = Solution()
print(s.convert2("PAYPALISHIRING", 3))
