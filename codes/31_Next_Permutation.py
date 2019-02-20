class Solution:
    def nextPermutation(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """

        lens = len(nums)
        i = lens - 1
        while i > 0:
            if nums[i - 1] >= nums[i]:
                i -= 1
            else:
                break
        if i == 0:
            nums[0:] = nums[::-1]
        else:
            j = i
            while j < lens - 1:
                if nums[j + 1] <= nums[i - 1]:
                    break
                else:
                    j += 1
            tmp = nums[j]
            nums[j] = nums[i - 1]
            nums[i - 1] = tmp
            nums[i:] = nums[i:][::-1]
        return nums


s = Solution()
print(s.nextPermutation([4, 2, 2, 1]))
