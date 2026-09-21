class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res =[[]]
        n = len(nums)

        def build(cur, idx):
            nonlocal res
            if idx >= n:
                return

            cur.append(nums[idx])
            res.append(cur[:])

            for i in range(idx+1, n):
                build(cur, i)
            if cur:
                cur.pop()
        
        for i in range(n):
            build([], i)
        return sorted(res)


