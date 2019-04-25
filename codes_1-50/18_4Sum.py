class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        if len(nums) < 4:
            return []

        nums = sorted(nums)
        outs = []
        i = 0
        while i < len(nums) - 3:
            j = len(nums) - 1

            while j > i + 2:
                k = i + 1
                w = j - 1
                while k < w:
                    sums = nums[i] + nums[j] + nums[k] + nums[w]
                    if sums < target:
                        k += 1
                    elif sums > target:
                        w -= 1
                    else:
                        outs.append([nums[i], nums[k], nums[w], nums[j]])
                        k += 1
                        w -= 1
                        while k < w and nums[k] == nums[k - 1]:
                            k += 1
                        while k < w and nums[w] == nums[w + 1]:
                            w -= 1

                j -= 1
                while j > i + 2 and nums[j] == nums[j + 1]:
                    j -= 1
            i += 1
            while i < len(nums) - 3 and nums[i - 1] == nums[i]:
                i += 1
        return outs


s = Solution()
# print(s.fourSum([1, 0, -1, 0, -2, 2], 0))
print(s.fourSum([-3, -1, 0, 2, 4, 5], 2))
