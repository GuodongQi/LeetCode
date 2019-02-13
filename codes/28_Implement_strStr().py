class Solution:
    def strStr(self, haystack: 'str', needle: 'str') -> 'int':
        if not len(needle):
            return 0

        h_start = 0
        while h_start < len(haystack) - len(needle) + 1:
            i = 0
            while i < len(needle) and h_start + i < len(haystack):
                if haystack[h_start + i] != needle[i]:
                    h_start += 1
                    break
                elif i != len(needle) - 1:
                    i += 1
                else:
                    return h_start
        return -1


class Solution2:
    def strStr(self, haystack: 'str', needle: 'str') -> 'int':
        if not needle:
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1


s = Solution()
print(s.strStr("mississippi", "isipi"))
print(s.strStr("hello", "ll"))
