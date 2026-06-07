from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, max_count  = 0,0
        for num in nums:
            if max_count == 0:
                res = num
            max_count += (1 if num == res else -1 )
        return res