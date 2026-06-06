class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list_set = set(nums)

        return len(list_set) != len(nums)
        