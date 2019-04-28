class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = len(s)
        if not l:
            return 0
        out = 0
        flag = 1
        for i in range(l - 1, -1, -1):
            if s[i] == ' ':
                if flag:
                    continue
                else:
                    break
            else:
                flag = 0
                out += 1
        return out
s = Solution()
print(s.lengthOfLastWord("Hello World"))