class Solution:
    def searchRange(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        size = len(nums)
        if size == 0:
            return [-1, -1]
        left = 0
        right = size - 1
        real_num = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                real_num = mid
                right = mid - 1
        if real_num < 0:
            return [-1, -1]
        start = real_num

        left = 0
        right = size - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                real_num = mid
                left = mid + 1
        end = real_num

        return [start, end]

s = Solution()
print(s.searchRange([10],10))
