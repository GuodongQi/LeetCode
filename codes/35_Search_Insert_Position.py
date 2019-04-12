class Solution:
    def searchInsert(self, nums: 'List[int]', target: int) -> 'int':
        start_pt = 0
        end_pt = len(nums) - 1
        mid_old = 0
        if nums[end_pt] < target:
            return end_pt + 1
        if nums[start_pt] > target:
            return 0
        while start_pt <= end_pt:
            mid = (start_pt + end_pt) // 2
            if nums[mid] > target:
                end_pt = mid
            elif nums[mid] < target:
                start_pt = mid
            else:
                return mid
            if mid_old == mid:
                return mid + 1
            mid_old = mid

s = Solution()
print(s.searchInsert([1], 0))