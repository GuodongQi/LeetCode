class Solution:
    def findSubstring(self, s: 'str', words: 'List[str]') -> 'List[int]':
        if not len(s) or not len(words):
            return []
        word_len = len(words[0])
        substr_len = word_len * len(words)
        dict1 = dict.fromkeys(words, 0)
        start_index = []

        for i in words:
            dict1[i] += 1

        dict2 = dict.fromkeys(words, 0)
        i = 0
        while i < len(s) - substr_len + 1:
            for j in range(i, substr_len + i, word_len):
                if not dict1.__contains__(s[j:j + word_len]):
                    i += j
                    dict2 = dict.fromkeys(words, 0)
                    break
                elif dict2[s[j:j + word_len]] < dict1[s[j:j + word_len]]:
                    dict2[s[j:j + word_len]] += 1
                else:
                    i += 1
                    dict2 = dict.fromkeys(words, 0)
                    break
            if dict2 == dict1:
                start_index.append(i)
        return start_index

    def findSubstring1(self, s: 'str', words: 'List[str]') -> 'List[int]':
        if not len(s) or not len(words):
            return []
        word_len = len(words[0])
        substr_len = word_len * len(words)
        dict1 = dict.fromkeys(words, 0)
        start_index = []
        for i in words:
            dict1[i] += 1

        for i in range(0, len(s) - substr_len + 1):
            dict2 = dict.fromkeys(words, 0)
            for j in range(i, substr_len + i, word_len):
                if not dict1.__contains__(s[j:j + word_len]):
                    break
                elif dict2[s[j:j + word_len]] < dict1[s[j:j + word_len]]:
                    dict2[s[j:j + word_len]] += 1
                else:
                    break
            if dict2 == dict1:
                start_index.append(i)

        return start_index


s = Solution()
print(s.findSubstring("barfoothefoobarman", ["foo", "bar"]))
print(s.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]))
print(s.findSubstring("aaa", ["a", "a"]))
