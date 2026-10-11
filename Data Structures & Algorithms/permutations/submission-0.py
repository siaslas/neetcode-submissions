class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        used = set()
        n = len(nums)
        res = []

        def dfs(cur_list):
            if len(cur_list) == n:
                res.append(cur_list[:])
            for num in nums:
                if num not in used:
                    cur_list.append(num)
                    used.add(num)
                    dfs(cur_list)
                    used.remove(num)
                    cur_list.pop()
        
        dfs([])
        return res



