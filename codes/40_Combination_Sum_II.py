class Solution:
    def combinationSum2(self, candidates: 'List[int]', tar: int) -> 'List[List[int]]':
        if not len(candidates):
            return [[]]
        candidates.sort()

        def bp(nums, target, index, path, res):
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return
            for j in range(index, len(nums)):
                if j > index and nums[j-1] == nums[j]:
                    continue
                bp(nums, target - candidates[j], j + 1, path + [candidates[j]], res)

        ress = []
        bp(candidates, tar, 0, [], ress)
        return ress