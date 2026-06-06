class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights) - 1
        max_cap = 0

        while L < R:
            max_cap = max(max_cap, min(heights[L], heights[R])*(R-L))

            if heights[L] >= heights[R]:
                R -= 1
            else:
                L += 1

        return max_cap
