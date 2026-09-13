class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)
        if k == n:
            return points
        
        def calcDistance(p):
            return math.sqrt(p[0]**2 + p[1]**2)

        max_heap = []
        for i in range(k):
            dist = calcDistance(points[i])
            heapq.heappush_max(max_heap, (dist, i))
        for j in range(k,n):
            dist = calcDistance(points[j])
            if dist < max_heap[0][0]:
                heapq.heappop_max(max_heap)
                heapq.heappush_max(max_heap, (dist, j))

        res = []
        for p in max_heap:
            res.append(points[p[1]])
        return res




        
