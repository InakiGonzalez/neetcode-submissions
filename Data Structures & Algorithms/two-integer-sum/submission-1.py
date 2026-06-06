class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for idx, val in enumerate(nums):
            diff = target - val
            if diff in nums_dict:
                return [nums_dict[diff], idx]
            nums_dict[val] = idx
        