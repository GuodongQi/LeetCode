class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)
        n_ = n
        state = [[0] * (n + 1) for i in range(m + 1)]
        if m != n and "*" not in p:
            return False

        for item in p:
            if "*" == item:
                n_ -= 2

        # 当s为空时 p不为空
        if not m:
            if not n:
                return True
            elif not n_:
                return True
            else:
                return False

        if n_ > m:
            return False

        # 初始化左上角
        state[0][0] = True
        # 初始化左列
        for i in range(1, m):
            state[i][0] = False
        # 初始化顶列
        for j in range(1, n):
            if p[j-1] == "*":
                state[0][j] = state[0][j - 2]
            else:
                state[0][j] = False

        # 递推关系
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j-1] == ".":
                    state[i][j] = state[i - 1][j - 1]
                elif p[j-1] == "*":
                    if p[j - 2] != s[i-1] and p[j - 2] != ".":
                        if j-1 < 2:
                            state[i][j] = False
                        else:
                            state[i][j] = state[i][j - 2]  # 如果x前的字符和当前字符不相同，那么将x赋值为0
                    else:
                        state[i][j] = state[i][j - 2] or state[i - 1][j] or state[i][j - 1]

                else:
                    state[i][j] = state[i - 1][j - 1] and s[i-1] == p[j-1]
        return state[m][n]


s = Solution()
print(s.isMatch("mississippi", "mis*is*ip*."))  # t
print(s.isMatch("aab", "c*a*b"))  # t
print(s.isMatch("ab", ".*"))  # t
print(s.isMatch("", ".*"))  # t
print(s.isMatch("a", "a*a"))  # T
print(s.isMatch("aa", "a*"))  # t
print(s.isMatch("aaa", "ab*ac*a"))  # t
print(s.isMatch("aaabaaaababcbccbaab", "c*c*.*c*a*..*c*"))  # t
print("------")
print(s.isMatch("issippi", "is*p*."))  # f
print(s.isMatch("abcd", "d*"))  # f
print(s.isMatch("sippi", "s*p*."))  # f
print(s.isMatch("abb", "b*"))  # f
print(s.isMatch("acbbcbcbcbaaacaac", "ac*.a*ac*.*ab*b*ac"))  # f
