class Solution:
    def isValid(self, s: str) -> bool:
        pars = {"}":"{", ")":"(", "]":"["}
        stack = []

        for c in s:
            if c not in pars:
                stack.append(c)
            else:
                if not stack or stack[-1] != pars[c]:
                    return False
                stack.pop()

        return not stack
                 