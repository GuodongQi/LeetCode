class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        num_list = []
        isneg = 0
        neg_flag = 0
        blank_flag = 0
        num_con = 0
        y = 0
        ground = - 2 ** 31
        flor = -ground - 1
        for item in str:
            if item == " " and not blank_flag:
                continue
            elif item == "-" and not neg_flag and not num_con:
                isneg = 1
                neg_flag = 1
                blank_flag = 1
            elif item == "+" and not neg_flag and not num_con:
                isneg = 0
                neg_flag = 1
                blank_flag = 1
            elif "0" <= item <= "9":
                num_list.append(item)
                blank_flag = 1
                num_con = 1
            else:
                break

        lens = len(num_list)
        for i, item in enumerate(num_list):
            y = y + int(item) * 10 ** (lens - i - 1)
        if isneg:
            y = -y
        if y < ground:
            y = ground
        elif y > flor:
            y = flor
        return y


s = Solution()
print(s.myAtoi("  -4-2 "))
