class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 0
        r = max(piles)

        while (l <= r):
            k = (l + r) // 2

            totalTime = 0
            if k == 0:
                return res
            for p in piles:
                totalTime += math.ceil(float(p)/k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        
        return res