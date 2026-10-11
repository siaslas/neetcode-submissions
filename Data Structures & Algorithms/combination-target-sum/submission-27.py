class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(cur_sum, cur_list, start):
            if cur_sum == target:
                res.append(cur_list[:])
                return
            for i in range(start, len(nums)):
                if cur_sum + nums[i] > target:
                    return
                cur_list.append(nums[i])
                cur_sum += nums[i]
                dfs(cur_sum, cur_list, i)
                cur_list.pop()
                cur_sum -= nums[i]
            
        dfs(0, [], 0)
        return res

