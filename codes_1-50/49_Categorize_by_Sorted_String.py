class Solution:
    def groupAnagrams(self, strs):
        word_num = [0] * 26
        out_dict = {}
        for per_str in strs:
            for per_char in per_str:
                word_num[ord(per_char) - ord("a")] += 1
            # if out_dict.get(tuple(word_num)) is None:
            #     out_dict[tuple(word_num)] = [per_str]
            # else:
            #     out_dict[tuple(word_num)].append(per_str)
            out_dict.setdefault(tuple(word_num), [per_str]).append(" " + per_str)
            word_num = [0] * 26

        return list(out_dict.values())

s = Solution()
s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])