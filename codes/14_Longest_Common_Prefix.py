class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefixs = ""
        i = 0
        while True:
            try:
                tmp = strs[0][i]
                for j in range(1, len(strs)):
                    if tmp != strs[j][i]:
                        return prefixs
                else:
                    i += 1
                    prefixs += tmp
            except:
                return prefixs


s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight"]))
