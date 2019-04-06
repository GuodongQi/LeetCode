class Solution:
    def myPow(self, x: float, n: int) -> float:

        inter_index = []

        if n == 0:
            return float(1)
        if n > 0:
            neg = 0
        else:
            neg = -1
            n = -n

        size = -1
        ans = x

        while n:
            n, r = divmod(n, 2)
            size += 1
            if r == 0:
                inter_index.append(2)
            else:
                inter_index.append(1)
        for i in range(size):
            index = size - 1 - i
            if inter_index[index] == 2:
                ans *= ans
            else:
                ans = ans * ans * x

        if neg:
            ans = 1 / ans
        return ans


s = Solution()
a = s.myPow(2, -2)
print(a)
