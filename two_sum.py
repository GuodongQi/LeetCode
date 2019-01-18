class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):  # for j in range(i, len(nums))
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None

    def twoSum_2(self, nums, target):
        """
        创建一个字典，判断字典里是否含有target-nums[i]
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, item in enumerate(nums):
            d[i] = item

        for i, item in enumerate(nums):
            if target - item in d.values() and list(d.values()).index(target - item) is not i:
                return [i, list(d.values()).index(target - item)]

        return None

# 经过测试，方法一 8120ms 方法二 2540ms
