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
        state = [[0] * n for i in range(m)]
        if m != n and "*" not in p:
            return False

        for item in p:
            if "*" == item:
                n_ -= 2

        # 当s为空时
        if not m:
            if not n:
                return True
            elif not n_:
                return True
            else:
                return False

        if n_ > m:
            return False

        # 初始化
        # for i in range(m):
        #     # if p[0] == "." or n > 1 and p[1] == "*":
        #     if p[0] == ".":
        #         state[i][0] = True
        #     else:
        #         state[i][0] = False
        if p[0] == ".":
            state[0][0] = True
        else:
            state[0][0] = s[0] == p[0][0]
        for i in range(1, m):
            state[i][0] = False

        for j in range(1, n):
            if p[j] == "*":
                if j - 2 < 0:
                    state[0][j] = True
                else:
                    state[0][j] = state[0][j - 2]
            elif p[j] == ".":
                state[0][j] = True
            else:
                state[0][j] = s[0]==p[j]

        # 递推关系
        for i in range(1, m):
            for j in range(1, n):
                if p[j] == ".":
                    state[i][j] = state[i - 1][j - 1]
                elif p[j] == "*":
                    if p[j - 1] != s[i] and p[j - 1] != ".":
                        if j < 2:
                            state[i][j] = False
                        else:
                            state[i][j] = state[i][j - 2]  # 如果x前的字符和当前字符不相同，那么将x赋值为0
                    else:
                        state[i][j] = state[i][j - 2] or state[i - 1][j] or state[i][j - 1]

                else:
                    state[i][j] = state[i - 1][j - 1] and s[i] == p[j]
        return state[m - 1][n - 1]


s = Solution()
# print(s.isMatch("mississippi", "mis*is*ip*.")) # t
# print(s.isMatch("issippi", "is*p*."))           # f
# print(s.isMatch("aab", "c*a*b"))                # t
# print(s.isMatch("abcd", "d*"))                  #f
# print(s.isMatch("sippi", "s*p*."))               #f
# print(s.isMatch("ab", ".*"))                    #t
# print(s.isMatch("", ".*"))                     #f
# print(s.isMatch("a", "a*a"))  # T
print(s.isMatch("abb", "b*"))  # T
