class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.even = True

    def addNum(self, num: int) -> None:
        if not self.max_heap:
            heapq.heappush(self.max_heap, -num)
        elif self.even:
            heapq.heappush(self.min_heap, num)
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        else:
            heapq.heappush(self.min_heap, num)
        
        if self.max_heap and self.min_heap and -self.max_heap[0] > self.min_heap[0]:
            left_value = -heapq.heappop(self.max_heap)
            right_value = heapq.heappop(self.min_heap)

            heapq.heappush(self.max_heap, -right_value)
            heapq.heappush(self.min_heap, left_value)

        self.even = not self.even

    def findMedian(self) -> float:
        if not self.max_heap:
            return float(0)
        
        if self.even:
            left, right = -self.max_heap[0], self.min_heap[0]
            return (left + right) / 2
        else:
            if self.min_heap:
                return float(min(-self.max_heap[0], self.min_heap[0]))
            else:
                return float(-self.max_heap[0])
            
        
        