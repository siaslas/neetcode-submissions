class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def dfs(cur_list, cur_sum, start):

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                cur_list.append(candidates[i])
                cur_sum += candidates[i]
                if cur_sum >= target:
                    if cur_sum == target:
                        res.append(cur_list[:])
                    cur_list.pop()
                    return
                dfs(cur_list, cur_sum, i+1)
                cur_list.pop()
                cur_sum -= candidates[i]

            return cur_sum
                
        dfs([], 0, 0)
        return res

