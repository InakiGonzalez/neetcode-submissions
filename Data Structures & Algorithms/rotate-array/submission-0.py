class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        def reverse(ls, l, r):
            while l <= r:
                tmp = ls[r]
                ls[r] = ls[l]
                ls[l] = tmp

                l+=1
                r-=1
            return ls

        reverse(nums, 0, n-1)
        reverse(nums,0,k-1)
        reverse(nums,k,n-1)
