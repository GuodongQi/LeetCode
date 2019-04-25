class Solution:
    def combinationSum(self, candidates: 'List[int]', target: 'int') -> 'List[List[int]]':
        if not len(candidates):
            return []

        def bp(candi, target, index, path, res):
            if target < 0:
                return
            if target == 0:
                res.append(path)  # if target == 0, it shows  that the path  is valid
                return
                # if target is not 0
            for i in range(index, len(candidates)):
                bp(candi, target - candi[i], i, path + [candi[i]], res)
        res = []
        bp(candidates, target, 0, [], res)
        return res

    # recursion
    # def dp(tar):
    #     if tar < candidates[0]:
    #         return None
    #     r_all = []
    #     for i in range(len(candidates)):
    #         if tar - candidates[i] == 0:
    #             r_all.append([candidates[i]])
    #         else:
    #             out = dp(tar - candidates[i])
    #             if out is not None:
    #                 r = [per_out + [candidates[i]] for per_out in out if len(per_out)]
    #                 r_all += r
    #     return r_all
    # all_out = set(dp(target))
    # return all_out


s = Solution()
print(s.combinationSum([2, 3, 6, 7], 7))
