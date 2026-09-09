class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        if nums:
            self.min_heap = nums[:k]
            heapq.heapify(self.min_heap)
        
            for i in range(k, len(nums)):
                if nums[i] > self.min_heap[0]:
                    heapq.heapreplace(self.min_heap, nums[i])

    def add(self, val: int) -> int:
        if len(self.min_heap) == self.k and val > self.min_heap[0]:
            heapq.heapreplace(self.min_heap, val)
        elif len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        return self.min_heap[0]


        
