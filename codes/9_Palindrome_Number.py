class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num_list = []
        if x < 0:
            return False
        while x:
            n = x % 10
            x = x //10
            num_list.append(n)

        for i in range(len(num_list)//2):
            if num_list[i] != num_list[len(num_list)-1 - i]:
                return False

        return True

s= Solution()
print(s.isPalindrome(121))