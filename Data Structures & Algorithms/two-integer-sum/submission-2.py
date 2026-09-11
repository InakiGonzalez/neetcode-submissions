class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for idx, val in enumerate(nums):
            if val in nums_dict:
                return [nums_dict[val], idx]
            nums_dict[target-val] = idx
        