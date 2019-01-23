class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_str = []
        symbols = ["I", "V", "X", "L", "C", "D", "M"]

        def d_symbols(_num, _symble):
            """
            :param _num: 余数
            :param _symble: 根据余数确定循环输出的罗马数
            :return:
            """
            out = []
            for i in range(_num):
                out.append(_symble)
            return "".join(out)

        k = 0  # 处理的当前的位数

        while num:
            num, mod = divmod(num, 10)
            if 5 <= mod < 9:
                strs = "".join([symbols[2 * k + 1], d_symbols(mod - 5, symbols[2 * k])])
                roman_str.append(strs)
            elif mod == 9:
                strs = "".join([symbols[2 * k], symbols[2 * k + 2]])
                roman_str.append(strs)
            elif mod == 4:
                strs = "".join([symbols[2 * k], symbols[2 * k + 1]])
                roman_str.append(strs)
            else:
                roman_str.append(d_symbols(mod, symbols[2 * k]))
            k += 1
        return "".join(roman_str[::-1])


s = Solution()
print(s.intToRoman(1994))
print(s.intToRoman(58))
print(s.intToRoman(9))
print(s.intToRoman(4))
print(s.intToRoman(3))
