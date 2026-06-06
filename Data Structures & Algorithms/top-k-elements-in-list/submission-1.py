class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            counts[n] = 1 + counts.get(n,0)
        counts = sorted(counts.items(), key=lambda item:item[1], reverse=True)
        most_frequent = [item[0] for item in counts]
        return most_frequent[:k]
        