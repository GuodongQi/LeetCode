class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums = sorted(nums)
        if len(nums) < 3:
            return []
        i = 0
        sum_num = nums[i] + nums[i + 1] + nums[i + 2]
        closest = sum_num - target
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1

            while j < k:
                sum_num = nums[i] + nums[j] + nums[k]
                close = sum_num - target

                if close < 0:
                    if abs(close) < abs(closest):
                        closest = close
                    j += 1
                elif close > 0:
                    if abs(close) < abs(closest):
                        closest = close
                    k -= 1
                else:
                    return target
            i += 1
            while i < len(nums) and nums[i - 1] == nums[i]:
                i += 1

        return closest + target


s = Solution()
print(s.threeSumClosest([-1, 2, 1, -4], 1))
