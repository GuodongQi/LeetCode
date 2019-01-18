class Solution:
    def lengthOfLongestSubstring(self, s):  # too_slow
        """
        :type s: str
        :rtype: int
        """
        if not len(s):
            return 0
        longest = s[0]
        tmp = []
        i0 = 0  # begin index
        i1 = 0  # end index
        while i1 < len(s):
            item = s[i1]
            if item not in tmp:
                tmp.append(item)
                i1 = i1 + 1
            elif len(longest) < len(tmp):
                longest = tmp
                i0 = i0 + 1
                tmp = []
                i1 = i0
            else:
                i0 = i0 + 1
                tmp = []
                i1 = i0
        if len(longest) < len(tmp):
            longest = tmp
        return len(longest)

    def lengthOfLongestSubstring_2(self, s):  # slid_windows
        if not len(s):
            return 0
        longest = 0
        tmp = []
        i0 = 0  # begin index
        i1 = 0  # end index
        while i1 < len(s):
            item = s[i1]
            if item not in tmp:
                tmp.append(item)
                i1 = i1 + 1
            elif longest < len(tmp):
                longest = len(tmp)
                i0 = i0 + 1
                tmp = tmp[1:]
                i1 = i0 + len(tmp)
            else:
                i0 = i0 + 1
                tmp = tmp[1:]
                i1 = i0 + len(tmp)
        if longest < len(tmp):
            longest = len(tmp)
        print( longest)


s1 = Solution
string = "anviaj"
s1.lengthOfLongestSubstring_2(s1, string)
