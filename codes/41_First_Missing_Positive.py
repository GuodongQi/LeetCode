class Solution:
    def firstMissingPositive(self, nums: 'List[int]') -> int:
        i = 0
        l = len(nums)

        while i < l:
            while i < l and nums[i] != i + 1:
                if nums[i] < 0 or nums[i] > l:
                    nums[i] = 0
                    break
                if nums[i] == 0:
                    break
                tmp = nums[i]
                nums[i] = nums[tmp - 1]
                nums[tmp - 1] = tmp

                # if nums[i] < 0 or nums[i] > l:
                #     nums[i] = 0
                #     i += 1
                # nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
            i += 1
        return nums


s = Solution()
print(s.firstMissingPositive([2, 7, 5, 3, -1, 1, 6, 8]))
