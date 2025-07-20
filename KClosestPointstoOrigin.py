class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        res = []
        for x, y in points:
            distance = sqrt((0-x)**2 + (0-y)**2)
            heapq.heappush(heap, (distance, [x, y]))
                
        for i in range(k):
            dist, arr = heapq.heappop(heap)
            res.append(arr)
        
        return res
        
