class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # math formula : position + x*speed = target
        # x = (target-position) / speed
        # fleets can also be explained in cycles taken to arrive to target
        # cycles are given by x above
        # we group our fleets by the different values of x ina dict, and return the amount of keys (fleets)

        pairs = zip(position,speed)
        pairs = sorted(pairs, reverse=True)
        stack = []
        for p,s in pairs:
            stack.append((target - p)/s)
            if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)