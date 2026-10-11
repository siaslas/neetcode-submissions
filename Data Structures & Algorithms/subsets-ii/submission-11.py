class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        n = len(nums)
        nums.sort()
        
        def dfs(subset, start):
            res.append(subset[:])

            for i in range(start, n):
                if i > start and nums[i] == nums[i-1]:
                    continue
                subset.append(nums[i])
                dfs(subset, i+1)
                subset.pop()
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            dfs([nums[i]], i+1)
            
        return res


