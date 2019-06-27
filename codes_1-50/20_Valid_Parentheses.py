class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not len(s):
            return True
        if len(s) == 1:
            return False

        bracks = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for item in s:
            if item in bracks:
                stack.append(bracks[item])
            else:
                if not stack:
                    return False
                if item == stack.pop():
                    continue
                else:
                    return False
        if len(stack):
            return False
        else:
            return True

    def isValid1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = list(s)
        if not len(s):
            return True
        if len(s) == 1:
            return False
        open_bracks = ["(", "[", "{"]
        # close_bracks = [")", "]", "}"]
        #
        # open_brack_index = 0
        # close_brack_index = 1

        while s:
            for i in range(len(s)):
                if s[i] in open_bracks:
                    if i == len(s) - 1:
                        return False
                    continue
                if s[i] == ")" and s[i - 1] == "(" or \
                        s[i] == "}" and s[i - 1] == "{" \
                        or s[i] == "]" and s[i - 1] == "[":
                    s.pop(i)
                    s.pop(i - 1)
                    break
                else:
                    return False
        return True


s = Solution()
# print(s.isValid("()[]{}"))
print(s.isValid("((("))
print(s.isValid("){"))

print(s.isValid("()"))
