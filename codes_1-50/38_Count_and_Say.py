class Solution:
    def countAndSay(self, n: int) -> str:
        ans = '1'
        for i in range(n-1):
            j = 0
            tmp = ''
            while j < len(ans):
                count = 1
                while j + 1 < len(ans) and ans[j + 1] == ans[j]:
                    count += 1
                    j += 1
                tmp += str(count) + ans[j]
                j += 1
            ans = tmp
        return ans

s = Solution()
print(s.countAndSay(5))