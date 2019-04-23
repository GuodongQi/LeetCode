class Solution:
    def permuteUnique(self, nums: 'List[int]') -> 'List[List[int]]':
        nums = sorted(nums)

        # def dfs(nums, index, path, res):
        #     for i in range(index, len(nums)):
        #
        #     return

        # def myiter(mynums):
        #     if not len(mynums):
        #         return []
        #     if len(mynums) == 1:
        #         return [mynums]
        #     ans = myiter(mynums[:-1])
        #     new_ans = []
        #     for per_ans in ans:
        #         for i in range(len(per_ans) + 1):
        #             new_ans.append(per_ans[:i] + [mynums[-1]] + per_ans[i:])
        #             if i < len(per_ans) and per_ans[i] == mynums[-1]:
        #                 break
        #     return new_ans

        # def myiter(mynums):
        #     if not len(mynums):
        #         return []
        #     if len(mynums) == 1:
        #         return [mynums]
        #     dict_tmp = {}
        #     tmp = myiter(mynums[:-1])
        #     for per_item in tmp:  # such as [1, 1, 2, 3]
        #         for i in range(len(per_item) + 1):
        #             per_item_tmp = per_item.copy()
        #             per_item_tmp.insert(i, mynums[-1])
        #             dict_tmp.setdefault(tuple(per_item_tmp), True)
        #     return list(map(list, dict_tmp.keys()))

        return myiter(nums)


s = Solution()
print(s.permuteUnique([2, 1, 1, 2]))
