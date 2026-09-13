from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dict with num: freq
        # sort the dict by freqs, desc
        # output the k first
        res = []
        nums_count = Counter(nums)
        nums_count = dict(sorted(nums_count.items(), key=lambda x: x[1], reverse=True))
        for val in nums_count.keys():
            res.append(val)
        return res[:k]