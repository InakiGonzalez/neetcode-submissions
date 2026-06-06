class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        og_length = len(nums)   
        new_length = len(set(nums))
        return og_length != new_length
