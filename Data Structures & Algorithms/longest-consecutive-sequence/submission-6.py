class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        [2,20,4,10,3,4,5]
        [2,3,4,4,5,10,20] -> set()


        [2,3,4,5,10,20]
                     ^
                    i = 5
                    largest_sf=0
                    max_len=4

        [20,10,5,4,3,2]
        [20,10,5,4,3,2]
        '''
        setNums = set(nums)
        longest = 0

        for n in nums:
            if (n-1) not in setNums:
                length = 0
                while (n + length) in setNums:
                    length += 1
                longest = max(length, longest)
        return longest

