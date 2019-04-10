class Solution:
    def jump(self, nums):

        def dp(mynums):
            if len(mynums) == 0:
                return [0]
            if len(mynums) == 1:
                return [0]
            sol_list = dp(mynums[:-1])
            best_step = sol_list[-1] + 1
            for i in range(0, len(sol_list)):
                if i + nums[i] >= len(sol_list):
                    tmp = sol_list[i] + 1
                    if tmp < best_step:
                        best_step = tmp
            sol_list.append(best_step)
            return sol_list

        return dp(nums)


s = Solution()
print(s.jump([2, 3, 1, 1, 4]))
