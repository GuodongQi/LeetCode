class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums = sorted(nums)
        outs = []
        if len(nums) < 3:
            return []
        i = 0
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1

            while j < k:
                sum_num = nums[i] + nums[j] + nums[k]
                if sum_num < 0:
                    j += 1
                elif sum_num > 0:
                    k -= 1
                else:
                    outs.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j - 1] == nums[j]:
                        j += 1
                    while j < k and nums[k + 1] == nums[j]:
                        k -= 1
            i += 1
            while i < len(nums) and nums[i - 1] == nums[i]:
                i += 1

        return outs

    def threeSum2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums = sorted(nums)
        outs = []
        if len(nums) < 3:
            return []
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                sum_num = nums[i] + nums[j] + nums[k]
                if sum_num < 0:
                    j += 1
                elif sum_num > 0:
                    k -= 1
                elif [nums[i], nums[j], nums[k]] not in outs:
                    outs.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                else:
                    j += 1
                    k -= 1

            return outs

    def threeSum1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums = sorted(nums)

        dicts = {}
        for i, item in enumerate(nums):
            dicts[item] = i
        outs = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                a = nums[i]
                b = nums[j]
                if -(a + b) in dicts.keys() and dicts[-(a + b)] > j and [a, b, -a - b] not in outs:
                    outs.append([a, b, -a - b])
        return outs


s = Solution()
print(s.threeSum([0, 0, 0, 0]))
