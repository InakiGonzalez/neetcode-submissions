class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # dups are not an issue since we only want to reorder in place and return
        # len of nums different from val
        # negatives don't matter since we have a targer num
        # empty arrays will not affect the logic since we will have a for loop
        # ranging from 0 to len(nums) and return k afterwards (initialized as 0)
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k +=1
        return k
