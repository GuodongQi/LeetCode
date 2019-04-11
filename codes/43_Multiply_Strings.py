class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        str1_len = len(num1)
        str2_len = len(num2)
        result = [0] * (str2_len + str1_len)
        for i in range(str1_len - 1, -1, -1):
            for j in range(str2_len - 1, -1, -1):
                int_num1 = ord(num1[i]) - ord('0')
                int_num2 = ord(num2[j]) - ord('0')
                result[i + j + 1] += int_num1 * int_num2
                div, result[i + j + 1] = divmod(result[i + j + 1], 10)
                result[i + j] += div
        flag = 0
        ans = ""
        for i in range(len(result)):
            if result[i] != 0:
                flag = 1
            if flag == 1:
                ans += chr(ord('0') + result[i])
        return ans


s = Solution()
print(s.multiply("99999", "99"))
