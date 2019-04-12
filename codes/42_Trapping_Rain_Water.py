class Solution:

    def trap(self, height: 'List[int]') -> int:
        size = len(height)
        start_pt = 0
        end_pt = size - 1
        ans = 0
        while start_pt < end_pt:
            if height[start_pt] < height[end_pt]:
                i = 1
                while height[start_pt + i] < height[start_pt]:
                    ans += height[start_pt] - height[start_pt + i]
                    i += 1
                start_pt += i
            else:
                j = 1
                while height[end_pt - j] < height[end_pt]:
                    ans += height[end_pt] - height[end_pt - j]
                    j += 1
                end_pt -= j

        return ans

    # def trap(self, height: 'List[int]') -> int:
    #     size = len(height)
    #     if not size:
    #         return 0
    #     start_pt = 0
    #     end_pt = size - 1
    #     max_height = max(height)
    #     ans = 0
    #     for i in range(max_height):
    #         while height[start_pt] <= i:
    #             start_pt += 1
    #         while height[end_pt] <= i:
    #             end_pt -= 1
    #         if start_pt >= end_pt:
    #             return ans
    #         for j in range(start_pt, end_pt):
    #             if height[j + 1] <= i:
    #                 ans += 1
    #     return ans


s = Solution()
print(s.trap([3, 2, 9, 5, 6, 7]))
