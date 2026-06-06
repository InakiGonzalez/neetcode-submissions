class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums = sorted(nums, reverse=True)
        res = 1
        for i in range(len(nums) - 1):
            freq = 1
            val = k
            print("val: ", val)
            for j in range(i+1, len(nums)):
                op = nums[i] - nums[j]
                print("op: ", op)
                if op <= val:
                    freq += 1
                    print("freq: ", freq)
                    res = max(res, freq)
                    print("res: ", res)
                    val = val - op 
        return res
                