class Solution:
    def maxSubArray(self, nums: 'List[int]') -> int:
        l = len(nums)
        if not l:
            return None
        for i in range(1,l):
            if nums[i -1] > 0:
                nums[i] += nums[i-1]
        return max(nums)