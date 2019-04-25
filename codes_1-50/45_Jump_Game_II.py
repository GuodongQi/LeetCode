class Solution:
    def jump(self, nums):
        level = 0
        i = 0
        current_max_index = 0
        if nums[0] == 0:
            return 0
        if len(nums) <= 2:
            return len(nums) - 1
        while i < len(nums) - 1:
            current_max = 0
            level += 1
            jump_max = nums[i]
            for j in range(jump_max):
                if i + j + 1 >= len(nums) - 1:
                    return level
                if j + i + 1 + nums[i + j + 1] > current_max:
                    current_max = j + i + 1 + nums[i + j + 1]
                    current_max_index = j
            i += current_max_index + 1
        return level

        # def dp(mynums):
        #     if len(mynums) == 0:
        #         return [0]
        #     if len(mynums) == 1:
        #         return [0]
        #     sol_list = dp(mynums[:-1])
        #     best_step = sol_list[-1] + 1
        #     for i in range(0, len(sol_list)):
        #         if i + nums[i] >= len(sol_list):
        #             tmp = sol_list[i] + 1
        #             if tmp < best_step:
        #                 best_step = tmp
        #     sol_list.append(best_step)
        #     return sol_list
        #
        # return dp(nums)


s = Solution()
print(s.jump([1]))
