class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
            
        heapq.heapify_max(stones)
        
        while stones:
            w1, w2 = heapq.heappop_max(stones), heapq.heappop_max(stones)

            if w2 < w1:
                heapq.heappush_max(stones, w1-w2)
            if len(stones) == 1:
                return stones[0]
        
        return 0
            


