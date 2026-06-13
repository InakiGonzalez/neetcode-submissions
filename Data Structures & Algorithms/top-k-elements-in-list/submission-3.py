import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        nums_c = Counter(nums)
        min_heap = []

        for item, freq in nums_c.items():
            heapq.heappush(min_heap, (freq,item))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        
        return [item for freq,item in min_heap]

