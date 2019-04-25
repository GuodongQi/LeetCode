class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dicts = {
            "1": "",
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        def combination(comb, digit):
            outs_tmp = []
            for i in dicts[digit]:
                for j in comb:
                    outs_tmp.append(j + i)
            return outs_tmp

        if not len(digits):
            return []
        comb = dicts[digits[0]]
        for i in digits[1:]:
            comb = combination(comb, i)
        return comb


s = Solution()
print(s.letterCombinations("23"))
