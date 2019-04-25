class Solution:
    def firstMissingPositive(self, nums: 'List[int]') -> int:
        i = 0
        l = len(nums)
        # if not l:
        #     return 1
        while i < l:
            while i < l and nums[i] != i + 1:
                if nums[i] < 0 or nums[i] > l or nums[i] == nums[nums[i] - 1]:
                    nums[i] = 0
                    break
                if nums[i] == 0:
                    break
                tmp = nums[i]
                nums[i] = nums[tmp - 1]
                nums[tmp - 1] = tmp
            i += 1
        for i, item in enumerate(nums):
            if item == 0:
                return i + 1
        return l + 1
        # if nums[i] < 0 or nums[i] > l:
        #     nums[i] = 0
        #     i += 1
        # nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]


s = Solution()
print(s.firstMissingPositive([1, 1]))
